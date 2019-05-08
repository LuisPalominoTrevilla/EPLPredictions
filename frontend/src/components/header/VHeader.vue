<template>
    <div>
        <img class="epl-logo" src="@/assets/premier-league.png" alt="">
        <team-listing></team-listing>
        <v-menu @addMargin="margin => this.$emit('addMargin', margin)"/>
    </div>
</template>

<script>
import VMenu from './VMenu.vue';
import TeamListing from './TeamListing.vue';

export default {
    components: {
        VMenu,
        TeamListing
    }
}
</script>

<style lang="scss" scoped>
.epl-logo {
    width: 7rem;
    z-index: 2;
    left: 0;
    top: 0;
    position: fixed;
}
</style>