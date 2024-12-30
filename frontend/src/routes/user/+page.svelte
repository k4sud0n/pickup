<script>
    import BottomNavigation from "../../components/BottomNavigation.svelte";
    import axios from "axios";
    import { writable } from "svelte/store";
    import { goto } from "$app/navigation";
    import { onMount } from "svelte";
    import toast from "svelte-french-toast";

    const user = writable(null);
    const isAuthenticated = writable(false);
    const apiUrl = import.meta.env.VITE_API_URL;

    const getCsrfToken = async () => {
        try {
            const response = await fetch(`${apiUrl}/users/csrf-token`, {
                credentials: "include",
            });
            const data = await response.json();
            return data.csrftoken;
        } catch (error) {
            goto("/user/login");
        }
    };

    const checkLoginStatus = async () => {
        const csrftoken = await getCsrfToken();
        try {
            const response = await axios.get(`${apiUrl}/users/`, {
                withCredentials: true,
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
                },
            });
            user.set(response.data.user);
            isAuthenticated.set(true);
        } catch (error) {
            user.set(null);
            isAuthenticated.set(false);
            goto("/user/login");
        }
    };

    const handleLogout = async (e) => {
        e.preventDefault();
        try {
            const csrftoken = await getCsrfToken();
            const response = await axios.post(
                `${apiUrl}/users/logout`,
                {},
                {
                    withCredentials: true,
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrftoken,
                    },
                },
            );
            if (response.status === 200) {
                user.set(null);
                isAuthenticated.set(false);
                toast.success("로그아웃 되었습니다");
                goto("/user/login");
            }
        } catch (error) {
            toast.error("로그아웃 실패");
        }
    };

    onMount(() => {
        checkLoginStatus();
    });
</script>

<div class="m-10 min-h-screen">
    <div class="flex items-center justify-between rounded border border-solid p-5">
        <div class="flex items-center">
            <img class="h-14 w-14 rounded-full bg-slate-200" src="https://placehold.co/400" alt="" />
            <div class="ml-3">
                <div class="text-lg font-bold">{$user?.username}</div>
                <div class="text-sm">후기 3개</div>
            </div>
        </div>
        <div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
            </svg>
        </div>
    </div>
    <div class="mt-5 flex justify-center rounded bg-slate-200 p-5">광고</div>
    <div class="mt-5 rounded border border-solid p-5">
        <div class="text-lg font-bold">나의 거래</div>
        <div class="mt-3">찜 목록</div>
        <div class="mt-3">
            <a href="/logout" on:click={handleLogout}>로그아웃</a>
        </div>
        <div class="mt-3">설정</div>
    </div>
</div>

<BottomNavigation />
