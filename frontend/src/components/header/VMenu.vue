<template>
    <b-nav ref="menu" class="menu" :class="fixMenu? 'fix' : ''">
        <b-nav-item>Premier League</b-nav-item>
        <b-nav-item>Predictions</b-nav-item>
        <b-nav-item>Stats</b-nav-item>
    </b-nav>
</template>

<script>
export default {
    data() {
        return {
            fixMenu: false,
            lastRecordPos: -1
        };
    },
    created () {
        window.addEventListener('scroll', this.handleScroll);
    },
    destroyed () {
        window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        handleScroll () {
            if (this.$refs.menu.offsetTop - window.scrollY < 0 && this.lastRecordPos === -1) {
                this.$emit('addMargin', this.$refs.menu.offsetHeight);
                this.lastRecordPos = window.scrollY;
                this.fixMenu = true;
            } else if (window.scrollY < this.lastRecordPos) {
                this.$emit('addMargin', 0);
                this.fixMenu = false;
                this.lastRecordPos = -1;
            }
        }
    },
}
</script>

<style lang="scss" scoped>
.menu {
    background-color: #38003c;
    padding-left: 10%;
    font-size: 1.1rem;

    &.fix {
        position: fixed;
        width: 100%;
        top: 0;
    }

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