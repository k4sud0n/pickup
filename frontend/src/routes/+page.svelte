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
                <div class="flex justify-center items-center bg-slate-200 min-h-72">사진</div>
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
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-7 h-7">
          <path d="M11.47 3.841a.75.75 0 0 1 1.06 0l8.69 8.69a.75.75 0 1 0 1.06-1.061l-8.689-8.69a2.25 2.25 0 0 0-3.182 0l-8.69 8.69a.75.75 0 1 0 1.061 1.06l8.69-8.689Z" />
          <path d="m12 5.432 8.159 8.159c.03.03.06.058.091.086v6.198c0 1.035-.84 1.875-1.875 1.875H15a.75.75 0 0 1-.75-.75v-4.5a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75V21a.75.75 0 0 1-.75.75H5.625a1.875 1.875 0 0 1-1.875-1.875v-6.198a2.29 2.29 0 0 0 .091-.086L12 5.432Z" />
        </svg>
        <div class="text-sm">홈</div>
    </div>
    <div class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-7 h-7">
          <path d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z" />
        </svg>
        <div class="text-sm">관심</div>
    </div>
    <div class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-7 h-7">
          <path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 9a.75.75 0 0 0-1.5 0v2.25H9a.75.75 0 0 0 0 1.5h2.25V15a.75.75 0 0 0 1.5 0v-2.25H15a.75.75 0 0 0 0-1.5h-2.25V9Z" clip-rule="evenodd" />
        </svg>
        <div class="text-sm">등록</div>
    </div>
    <div class="flex flex-col items-center">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-7 h-7">
          <path fill-rule="evenodd" d="M5.337 21.718a6.707 6.707 0 0 1-.533-.074.75.75 0 0 1-.44-1.223 3.73 3.73 0 0 0 .814-1.686c.023-.115-.022-.317-.254-.543C3.274 16.587 2.25 14.41 2.25 12c0-5.03 4.428-9 9.75-9s9.75 3.97 9.75 9c0 5.03-4.428 9-9.75 9-.833 0-1.643-.097-2.417-.279a6.721 6.721 0 0 1-4.246.997Z" clip-rule="evenodd" />
        </svg>
        <div class="text-sm">채팅</div>
    </div>
    <a href="/my">
        <div class="flex flex-col items-center">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-7 h-7">
              <path fill-rule="evenodd" d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z" clip-rule="evenodd" />
            </svg>
            <div class="text-sm">MY</div>
        </div>
    </a>
</footer>
