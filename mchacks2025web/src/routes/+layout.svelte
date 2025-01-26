<script lang="ts">
	import '../app.css';
    import Navbar from '$lib/components/Navbar.svelte';
    import Footer from '$lib/components/Footer.svelte';

	let { children } = $props();
</script>

<Navbar/>
{@render children()}
<Footer/>