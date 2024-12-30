<script>
    import axios from "axios";
    import { writable } from "svelte/store";
    import { goto } from "$app/navigation";
    import toast, { Toaster } from "svelte-french-toast";

    const user = writable(null);
    const isAuthenticated = writable(false);

    const getCsrfToken = async () => {
        try {
            const response = await fetch("http://localhost:8000/api/v1/users/csrf-token", {
                credentials: "include",
            });
            const data = await response.json();
            return data.csrftoken;
        } catch (error) {
            console.error("Failed to fetch CSRF token", error);
        }
    };

    const checkLoginStatus = async () => {
        const csrftoken = await getCsrfToken();
        try {
            const response = await axios.get("http://localhost:8000/api/v1/users/", {
                withCredentials: true,
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
                },
            });
            // 응답에서 받은 사용자 정보를 store에 저장
            user.set(response.data.user);
            isAuthenticated.set(true);
        } catch (error) {
            console.error("Error during login status check:", error);
            user.set(null);
            isAuthenticated.set(false);
        }
    };

    checkLoginStatus();
</script>

<div>{$user?.username}</div>

<Toaster />
