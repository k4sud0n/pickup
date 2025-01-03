export async function load({ params, fetch }) {
    const { username, itemId } = params;

    // API 호출
    const apiUrl = import.meta.env.VITE_API_URL;
    const response = await fetch(`${apiUrl}/board/${username}/${itemId}`);

    if (!response.ok) {
        return {
            status: response.status,
            error: new Error("Item not found"),
        };
    }

    const item = await response.json();

    // 데이터 반환
    return { item };
}
