<template>
  <div class="home">
     <!-- Left navigation -->
     <navigation-drawer :drawer="drawer"></navigation-drawer>
     <!-- Toolbar -->  
    <v-toolbar app fixed clipped-left  color="green darken-1" dark>
      <v-toolbar-side-icon @click.stop="toggleDrawer"></v-toolbar-side-icon>
      <v-toolbar-title>Plumlee Dashboard</v-toolbar-title>
      <div class="user" style="position:absolute;right:0px">Logged with user: <span style="font-weight:600">{{userName}}</span></div>
    </v-toolbar>
    <!-- Content -->
    <v-content fill-height>
      <v-container fluid fill-height>
        <v-layout justify-center align-center fill-height>
          <router-view ></router-view>
        </v-layout>
      </v-container>
    </v-content>
    <!-- Footer -->
    <v-footer app fixed>
      <span>yo bitches</span>
    </v-footer>
  </div>
</template>

<script>
import NavigationDrawer from '@/components/home/NavigationDrawer.vue'
import { mapActions } from 'vuex'
export default {
  name: 'Home',
  props: ['userId'],
  components: {
    NavigationDrawer
  },
  methods: {
    ...mapActions([
      'pullPlayers',
      'whoami'
    ]),
    toggleDrawer () {
      this.drawer = !this.drawer
    }
  },
  created () {
    console.log('created!')
    let self = this
    this.whoami().then((res) => {
      self.userName = res.data.user
    })
    this.pullPlayers().then((res) => {
      if (res.error) {
        //
      } else {
        console.log('res:', res.data.players)
      }
    })
  },
  data () {
    return {
      drawer: true,
      userName: ''
    }
  }
}
</script>

<style scoped>

</style>
