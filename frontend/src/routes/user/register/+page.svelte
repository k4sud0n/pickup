<script>
  import { goto } from '$app/navigation';
  import toast, { Toaster } from 'svelte-french-toast';

  let username = '';
  let password = '';

  const handleSubmit = async () => {
    const apiUrl = import.meta.env.VITE_API_URL;

    const response = await fetch(apiUrl + '/users/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
      const data = await response.json();
      goto('/user/register/success', { state: { username } });
    } else {
      const error = await response.json();
      toast.error(error.message);
    }
  };
</script>

<div class="m-10">
  <div class="flex items-center justify-between">
    <div class="text-2xl">회원가입</div>
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
      <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12"/>
    </svg>
  </div>
  <div>
    <div class="mt-5">아이디</div>
    <input type="text" bind:value={username} class="border border-gray-300 p-2 rounded mt-2 min-w-full" placeholder="아이디를 입력하세요">
    <div class="mt-5">비밀번호</div>
    <input type="password" bind:value={password} class="border border-gray-300 p-2 rounded mt-2 min-w-full" placeholder="비밀번호를 입력하세요">
  </div>
  <button class="mt-10 p-2 min-w-full rounded bg-blue-600 text-white" on:click={handleSubmit}>가입하기</button>
</div>

<Toaster />
