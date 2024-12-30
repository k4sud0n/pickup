<script>
    import axios from "axios";
    import { toastMessage } from "$lib/stores/toastStore";
    import { goto } from "$app/navigation";
    import toast, { Toaster } from "svelte-french-toast";

    let username = "";
    let password = "";

    const handleSubmit = async () => {
        try {
            const csrfResponse = await axios.get("http://localhost:8000/api/v1/users/csrf-token", {
                withCredentials: true,
            });
            const csrfToken = csrfResponse.data.csrftoken;

            const response = await axios.post(
                "http://localhost:8000/api/v1/users/login",
                { username, password },
                {
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrfToken,
                    },
                    withCredentials: true,
                },
            );

            if (response.status === 200) {
                const checkSession = await axios.get("http://localhost:8000/api/v1/users/", {
                    withCredentials: true,
                    headers: {
                        "X-CSRFToken": csrfToken,
                    },
                });

                toast.success("로그인 성공!");
                goto("/");
            }
        } catch (error) {
            toast.error(error.response?.data?.message || "로그인 실패");
        }
    };
</script>

<div class="m-10">
    <div class="flex items-center justify-between">
        <div class="text-2xl">Pickup</div>
        <a href="/" aria-label="Go to homepage">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
            </svg>
        </a>
    </div>
    <div>
        <div class="mt-5">아이디</div>
        <input type="text" bind:value={username} class="mt-2 min-w-full rounded border border-gray-300 p-2" placeholder="아이디를 입력하세요" />
        <div class="mt-5">비밀번호</div>
        <input type="password" bind:value={password} class="mt-2 min-w-full rounded border border-gray-300 p-2" placeholder="비밀번호를 입력하세요" />
    </div>
    <button class="mt-10 min-w-full rounded bg-blue-600 p-2 text-white" on:click={handleSubmit}>로그인</button>
</div>

<Toaster />
