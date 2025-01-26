import { writable } from "svelte/store";

export const messages = writable([]);
export let socket;

export function connectWebSocket(url) {
    socket = new WebSocket(url);

    socket.onopen = () => console.log("WebSocket connected");
    socket.onmessage = (event) => {
        messages.update((msgs) => [...msgs, event.data]);
    };
    socket.onclose = () => console.log("WebSocket disconnected");
}

export function sendMessage(message) {
    if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(message);
    }
}
