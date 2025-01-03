<script>
    import { onMount } from "svelte";
    import { toastMessage } from "$lib/stores/toastStore";
    import { timeSince } from "$lib/utils";

    import toast, { Toaster } from "svelte-french-toast";

    import HeaderNavigation from "../components/HeaderNavigation.svelte";
    import BottomNavigation from "../components/BottomNavigation.svelte";

    // API URL
    const apiUrl = import.meta.env.VITE_API_URL;

    // Media URL
    const mediaUrl = import.meta.env.VITE_MEDIA_URL;

    // 데이터를 저장할 리스트
    let list = [];

    // 데이터 가져오기
    onMount(async () => {
        try {
            const response = await fetch(`${apiUrl}/board`);
            if (!response.ok) {
                throw new Error("데이터를 가져오는 데 실패했습니다.");
            }
            const data = await response.json();
            list = data.map((item) => ({
                id: item.id,
                name: item.name,
                author: item.author,
                price: Number(item.price), // price를 숫자로 변환
                createdAt: new Date(item.created_at), // created_at을 Date 객체로 변환
                like: item.likes,
                message: 0, // 메시지 수는 API 응답에 없으므로 기본값 0으로 설정
                image: `${mediaUrl}${item.image}`, // 이미지 URL
            }));
        } catch (error) {
            console.error("오류 발생:", error);
            toast.error("데이터를 불러오는 중 오류가 발생했습니다.");
        }
    });

    // 토스트 메시지 표시
    if ($toastMessage) {
        toast.success($toastMessage);
    }

    // 텍스트 자르기 함수
    function truncateText(text) {
        if (text.length > 30) {
            return text.substring(0, 30) + "...";
        }
        return text;
    }
</script>

<HeaderNavigation />

<div class="flex h-96 items-center justify-center bg-slate-200">광고</div>

<div class="my-10 flex justify-center">
    <div class="grid grid-cols-2 gap-10">
        {#each list as item, idx}
            <a href={`/@${item.author}/${item.id}`}>
                <div class="flex flex-col">
                    <div class="h-72 w-64">
                        <img src={item.image} alt={item.name} class="object-cover" />
                    </div>
                    <div>
                        <div class="mt-2 font-semibold">{item.price.toLocaleString()}원</div>
                        <div>{truncateText(item.name)}</div>
                        <div class="mt-1 flex justify-between text-sm text-slate-600">
                            <div>{timeSince(item.createdAt)}</div>
                            <div class="flex items-center">
                                <div class="mr-1 flex items-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mr-0.5 h-4 w-4">
                                        <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z"
                                        />
                                    </svg>
                                    <div>{item.like}</div>
                                </div>
                                <div class="flex items-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mr-0.5 h-4 w-4">
                                        <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z"
                                        />
                                    </svg>
                                    <div>{item.message}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        {/each}
    </div>
</div>

<BottomNavigation />

<Toaster />
