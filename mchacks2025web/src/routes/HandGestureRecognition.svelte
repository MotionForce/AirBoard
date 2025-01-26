<script lang="ts">
    import { onMount, onDestroy } from 'svelte';
    
    let videoElement: HTMLImageElement;
    let websocket: WebSocket;
    let handData: { left: number[][], right: number[][] } = { left: [], right: [] };
    let isConnected = false;
    let errorMessage = '';

    onMount(() => {
        connectWebSocket();
    });

    onDestroy(() => {
        if (websocket) {
            websocket.close();
        }
    });

    function connectWebSocket() {
        websocket = new WebSocket('ws://localhost:8765');

        websocket.onopen = () => {
            isConnected = true;
            errorMessage = '';
        };

        websocket.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                if (data.frame) {
                    videoElement.src = `data:image/jpeg;base64,${data.frame}`;
                }
                if (data.hand_data) {
                    handData = data.hand_data;
                }
            } catch (error) {
                console.error('Error processing message:', error);
            }
        };

        websocket.onerror = (error) => {
            errorMessage = 'WebSocket error occurred';
            console.error('WebSocket error:', error);
        };

        websocket.onclose = () => {
            isConnected = false;
            errorMessage = 'WebSocket connection closed';
            // Try to reconnect after 5 seconds
            setTimeout(connectWebSocket, 5000);
        };
    }
</script>

<div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Hand Gesture Recognition</h1>
    
    {#if errorMessage}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4" role="alert">
            <p>{errorMessage}</p>
        </div>
    {/if}
    
    <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1">
            <div class="bg-gray-100 p-4 rounded-lg">
                <h2 class="text-xl font-semibold mb-2">Camera Feed</h2>
                <img
                    bind:this={videoElement}
                    alt="Camera feed"
                    class="w-full rounded-lg shadow-lg"
                />
            </div>
        </div>
        
        <div class="flex-1">
            <div class="bg-gray-100 p-4 rounded-lg">
                <h2 class="text-xl font-semibold mb-2">Hand Data</h2>
                <div class="space-y-4">
                    <div>
                        <h3 class="font-medium">Left Hand</h3>
                        {#if handData.left.length > 0}
                            <pre class="bg-white p-2 rounded mt-1 text-sm overflow-x-auto">
                                {JSON.stringify(handData.left, null, 2)}
                            </pre>
                        {:else}
                            <p class="text-gray-500">No left hand detected</p>
                        {/if}
                    </div>
                    
                    <div>
                        <h3 class="font-medium">Right Hand</h3>
                        {#if handData.right.length > 0}
                            <pre class="bg-white p-2 rounded mt-1 text-sm overflow-x-auto">
                                {JSON.stringify(handData.right, null, 2)}
                            </pre>
                        {:else}
                            <p class="text-gray-500">No right hand detected</p>
                        {/if}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    pre {
        max-height: 200px;
    }
</style> 