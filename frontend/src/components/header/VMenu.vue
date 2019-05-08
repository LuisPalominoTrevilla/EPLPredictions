<template>
    <b-nav ref="menu" class="menu" :class="fixMenu? 'fix' : ''">
        <b-nav-item :class="{'active': currentView === '/'}" @click="pushRoute('/')">Premier League</b-nav-item>
        <b-nav-item :class="{'active': currentView === '/predictions'}" @click="pushRoute('/predictions')">Predictions</b-nav-item>
        <b-nav-item :class="{'active': currentView === '/playground'}" @click="pushRoute('/playground')">Playground</b-nav-item>
        <b-nav-item :class="{'active': currentView === '/positions'}" @click="pushRoute('/positions')">Standings</b-nav-item>
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
    computed: {
        currentView() {
            return this.$route.path;
        }
    },
    methods: {
        handleScroll () {
            this.$emit('getOffset', this.$refs.menu.offsetTop - window.scrollY);
            if (this.$refs.menu.offsetTop - window.scrollY < 0 && this.lastRecordPos === -1) {
                this.$emit('addMargin', this.$refs.menu.offsetHeight);
                this.lastRecordPos = window.scrollY;
                this.fixMenu = true;
            } else if (window.scrollY < this.lastRecordPos) {
                this.$emit('addMargin', 0);
                this.fixMenu = false;
                this.lastRecordPos = -1;
            }
        },

        pushRoute(route) {
            this.$router.push(route);
        }
    },
}
</script>

<style lang="scss" scoped>
.menu {
    z-index: 2;
    background-color: #38003c;
    padding-left: 12rem;
    font-size: 1.1rem;

    &.fix {
        position: fixed;
        width: 100%;
        top: 0;
    }

    .nav-item {
        position: relative;

        &.active:after {
            content: "";
            display: block;
            border: 6px solid transparent;
            border-bottom-color: #eaff04;
            position: absolute;
            bottom: 0;
            left: 50%;
            margin-left: -6px;
        }

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

        &.active .nav-link {
            &:hover:before {
                height: 0;
                z-index: -1;
            }
        }
    }
}
</style>