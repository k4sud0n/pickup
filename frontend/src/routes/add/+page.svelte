<script>
    import axios from "axios";

    import BottomNavigation from "../../components/BottomNavigation.svelte";
    import toast, { Toaster } from "svelte-french-toast";

    // 입력 데이터를 저장할 변수
    let productName = "";
    let category = "";
    let description = "";
    let price = "";
    let imageFile = null; // 이미지 파일
    let imagePreview = null; // 이미지 미리보기 URL

    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
            imageFile = file;
            imagePreview = URL.createObjectURL(file); // 미리보기 URL 생성
        }
    };

    const getCookie = (name) => {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
    };

    const registerProduct = async () => {
        const apiUrl = import.meta.env.VITE_API_URL;
        const csrfToken = getCookie("csrftoken");

        // FormData 객체 생성
        const formData = new FormData();
        formData.append("name", productName);
        formData.append("description", description);
        formData.append("price", parseInt(price));
        formData.append("file", imageFile); // 파일 객체를 직접 추가

        try {
            const response = await axios.post(
                `${apiUrl}/board/create`,
                formData, // FormData 객체를 전송
                {
                    headers: {
                        "X-CSRFToken": csrfToken,
                    },
                    withCredentials: true,
                },
            );
            toast.success("상품이 등록되었습니다!");
        } catch (error) {
            console.error("오류 응답:", error.response.data); // 오류 상세 정보 확인
            toast.error("상품 등록에 실패했습니다.");
        }
    };
</script>

<div class="m-10">
    <div class="flex items-center justify-between">
        <div class="text-2xl">상품정보</div>
    </div>
    <div>
        <div class="mt-5">상품명</div>
        <input type="text" class="mt-2 min-w-full rounded border border-gray-300 p-2" placeholder="상품명을 입력하세요" bind:value={productName} />
        <div class="mt-5">카테고리</div>
        <select id="main-category" class="mt-2 w-full rounded border border-gray-300" bind:value={category}>
            <option value="" disabled selected>카테고리를 선택하세요</option>
            <option value="electric-guitar">일렉기타</option>
            <option value="pickup">- 픽업</option>
            <option value="neck-body-etc">- 넥/바디/부품류</option>
            <option value="acoustic-guitar">어쿠스틱 기타</option>
            <option value="classic-guitar">- 클래식 기타</option>
            <option value="ukulele">- 우쿠렐레</option>
        </select>
        <div class="mt-5">이미지</div>
        <input type="file" accept="image/*" class="mt-2 w-full rounded border border-gray-300 p-2" on:change={handleImageUpload} />
        {#if imagePreview}
            <div class="mt-2">
                <img src={imagePreview} alt="미리보기" class="h-auto max-w-full rounded" />
            </div>
        {/if}
        <div class="mt-5">설명</div>
        <textarea
            class="mt-2 h-44 min-w-full resize-none rounded border border-gray-300 p-2"
            placeholder="브랜드, 모델명, 구매 시기, 하자 유무 등 상품 설명을 최대한 자세히 적어주세요.&#13;전화번호, SNS 계정 등 개인정보 입력은 제한될 수 있습니다."
            bind:value={description}
        ></textarea>
    </div>
</div>

<div class="m-10">
    <div class="flex items-center justify-between">
        <div class="text-2xl">가격</div>
    </div>
    <div class="mt-5 flex items-center">
        <div class="text-lg">₩</div>
        <input type="number" class="ml-2 flex-grow rounded border border-gray-300 p-2" placeholder="가격을 입력하세요" bind:value={price} />
    </div>
    <button class="mt-10 w-full rounded bg-blue-600 p-2 text-white" on:click={registerProduct}> 등록하기 </button>
</div>

<BottomNavigation />

<Toaster />
