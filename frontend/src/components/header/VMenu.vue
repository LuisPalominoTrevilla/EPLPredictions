<template>
    <b-nav class="menu">
        <b-nav-item>Premier League</b-nav-item>
        <b-nav-item>Predictions</b-nav-item>
        <b-nav-item>Stats</b-nav-item>
    </b-nav>
</template>

<script>
export default {
    
}
</script>

<style lang="scss" scoped>
.menu {
    background-color: #38003c;
    padding-left: 10%;
    font-size: 1.1rem;

    .nav-item {
        position: relative;
        .nav-link {
            color: #ffffff;
            text-decoration: none;
            padding-top: 1rem;
            padding-bottom: 1rem;

            &:before {
                content: "";
                display: block;
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 0;
                z-index: -1;
                transition: .2s;
                background-color: #e90052;
            }
            
            &:hover:before {
                height: 4px;
                z-index: 0;
            }
        }   
    }
}
</style>