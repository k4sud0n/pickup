<script>
    const list = [
        {id: 1, name: '쉑터 schecter banshee extreme fr 123123', price: 500000, createdAt: new Date(2024, 11, 26, 0, 0, 0), like: 2, message: 1},
        {id: 2, name: '쉑터 schecter banshee extreme fr', price: 700000, createdAt: new Date(2024, 9, 26, 0, 0, 0), like: 5, message: 2},
        {id: 3, name: '쉑터 schecter banshee extreme fr', price: 700000, createdAt: new Date(2024, 9, 26, 0, 0, 0), like: 5, message: 2},
    ]

    function timeSince(createdAt) {
        const now = new Date();
        const diffMs = now - createdAt; // 시간 차이 (밀리초)
        const diffSec = Math.floor(diffMs / 1000); // 초 단위
        const diffMin = Math.floor(diffSec / 60); // 분 단위
        const diffHours = Math.floor(diffMin / 60); // 시간 단위
        const diffDays = Math.floor(diffHours / 24); // 일 단위
        const diffMonths = Math.floor(diffDays / 30); // 월 단위 (평균 30일 기준)
        const diffYears = Math.floor(diffDays / 365); // 년 단위

        if (diffYears > 0) return `${diffYears}년 전`;
        if (diffMonths > 0) return `${diffMonths}달 전`;
        if (diffDays > 0) return `${diffDays}일 전`;
        if (diffHours > 0) return `${diffHours}시간 전`;
        if (diffMin > 0) return `${diffMin}분 전`;
        return `${diffSec}초 전`;
    }

    function truncateText(text) {
        if (text.length > 30) {
          return text.substring(0, 30) + '...';
        }
        return text;
    }
</script>

<header>
    <div class="flex m-5 justify-between items-center font-bold">
        <div class="text-xl">Pickup</div>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
        </svg>
    </div>
</header>

<div class="flex justify-center items-center bg-slate-200 h-96">
    광고
</div>

<div class="flex justify-center mt-10">
    <div class="grid grid-cols-2 gap-10">
        {#each list as item, idx}
            <div class="flex flex-col">
                <div class="flex justify-center items-center bg-slate-200 w-64 h-72">사진</div>
                <div>
                    <div class="font-semibold mt-2">{item.price.toLocaleString()}원</div>
                    <div>{truncateText(item.name)}</div>
                    <div class="flex justify-between text-slate-600 text-sm mt-1">
                        <div>{timeSince(item.createdAt)}</div>
                        <div class="flex items-center">
                            <div class="flex items-center mr-1">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4 mr-0.5">
                                  <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                                </svg>
                                <div>{item.like}</div>
                            </div>
                            <div class="flex items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4 mr-0.5">
                                  <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z" />
                                </svg>
                                <div>{item.message}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div>

<footer class="bg-white border-t-[1px] sticky bottom-0 w-full h-16 flex justify-around items-center">
    <div class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
        </svg>
        <div class="text-sm">홈</div>
    </div>
    <div class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
        </svg>
        <div class="text-sm">관심</div>
    </div>
    <div class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
        </svg>
        <div class="text-sm">등록</div>
    </div>
    <div class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 0 1-.923 1.785A5.969 5.969 0 0 0 6 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337Z" />
        </svg>
        <div class="text-sm">채팅</div>
    </div>
    <div class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-7 h-7">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
        </svg>
        <div class="text-sm">MY</div>
    </div>
</footer>
