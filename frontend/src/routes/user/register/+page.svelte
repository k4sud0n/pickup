<script>
    import axios from "axios";
    import { goto } from "$app/navigation";
    import toast, { Toaster } from "svelte-french-toast";

    let username = "";
    let password = "";
    let confirmPassword = "";

    const handleSubmit = async () => {
        const apiUrl = import.meta.env.VITE_API_URL;

        try {
            const response = await axios.post(apiUrl + "/users/register", {
                username,
                password,
                confirm_password: confirmPassword,
            });

            if (response.status >= 200 && response.status < 300) {
                goto("/user/register/success", { state: { username } });
            }
        } catch (error) {
            if (error.response && error.response.data) {
                toast.error(error.response.data.message);
            } else {
                toast.error("알 수 없는 오류가 발생했습니다.");
            }
        }
    };
</script>

<div class="m-10">
    <div class="flex items-center justify-between">
        <div class="text-2xl">회원가입</div>
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
        <div class="mt-5">비밀번호 확인</div>
        <input type="password" bind:value={confirmPassword} class="mt-2 min-w-full rounded border border-gray-300 p-2" placeholder="비밀번호를 입력하세요" />
    </div>
    <button class="mt-10 min-w-full rounded bg-blue-600 p-2 text-white" on:click={handleSubmit}>가입하기</button>
</div>

<Toaster />
