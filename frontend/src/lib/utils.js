// 시간 차이 계산 함수
export function timeSince(createdAt) {
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
