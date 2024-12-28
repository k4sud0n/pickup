<script>
      import { page } from '$app/stores';
      const { state } = $page;
      const username = state?.username || '사용자';
</script>

<div class="flex flex-col items-center justify-center h-screen">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="text-green-600 w-10 h-10">
      <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
    </svg>
    <h1 class="text-3xl font-bold text-green-600 mt-4">회원가입 성공!</h1>
    <p class="mt-4 text-lg">환영합니다, {username}님</p>
    <a href="/" class="mt-6 text-blue-600 underline">홈으로 돌아가기</a>
</div>
