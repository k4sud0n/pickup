<script>
    import { timeSince } from "$lib/utils";

    import BottomNavigation from "../../../components/BottomNavigation.svelte";

    export let data;
    const item = data.item;

    const mediaUrl = import.meta.env.VITE_MEDIA_URL;

    item.image = mediaUrl + item.image;
</script>

{#if item}
    <div>
        <div class="h-96 min-w-full bg-slate-200">
            <img src={item.image} alt={item.name} class="h-full w-full object-cover" />
        </div>
        <div class="m-10">
            <div class="text-xl font-bold">{item.name}</div>
            <div class="mt-2 text-lg">{item.price.toLocaleString()}원</div>
            <div class="flex items-center justify-between">
                <div class="mt-2">{timeSince(new Date(item.created_at))}</div>
                <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="mr-0.5 h-4 w-4">
                        <path
                            d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z"
                        />
                    </svg>
                    <div class="mr-1">{item.likes}</div>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="mr-0.5 h-4 w-4">
                        <path
                            fill-rule="evenodd"
                            d="M5.337 21.718a6.707 6.707 0 0 1-.533-.074.75.75 0 0 1-.44-1.223 3.73 3.73 0 0 0 .814-1.686c.023-.115-.022-.317-.254-.543C3.274 16.587 2.25 14.41 2.25 12c0-5.03 4.428-9 9.75-9s9.75 3.97 9.75 9c0 5.03-4.428 9-9.75 9-.833 0-1.643-.097-2.417-.279a6.721 6.721 0 0 1-4.246.997Z"
                            clip-rule="evenodd"
                        />
                    </svg>
                    <div>0</div>
                </div>
            </div>
        </div>
        <hr />
        <div class="m-10">{item.description}</div>
        <hr />
        <div class="m-10 flex justify-around gap-4">
            <button class="flex-1 rounded bg-blue-600 p-2 text-white">구매하기</button>
            <button class="flex-1 rounded bg-blue-600 p-2 text-white">채팅하기</button>
        </div>
    </div>
{:else}
    <div>Loading...</div>
{/if}

<BottomNavigation />
