<template>
  <v-layout row wrap justify-center align-center>
    <v-flex xs12 md5 text-xs-center>
      <v-card class="pa-3">
        <h2 class="green--text darken-1">Register to plumlee [{{getUser}}]</h2>
        <v-layout row wrap justify-center>
          <v-flex xs10 md10>
            <v-form v-model="valid" ref="form" lazy-validation>    
              <v-text-field label="User" v-model="userName" :rules="userRules" required></v-text-field>
              <v-text-field label="Password" type="password" name="password" v-model="password" :rules="passwordRules" required></v-text-field>
               <v-btn @click="submit" :disabled="!valid" color="primary">submit</v-btn>               
            </v-form>
          </v-flex>
        </v-layout>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'Signup',
  methods: {
    ...mapActions([
      'register',
      'login'
    ]),
    submit () {
      let data = {user: this.userName, password: this.password}
      this.register(data).then((res) => {
        console.log(res)
      })
    },
    clear () {
      this.$refs.form.reset()
    }
  },
  computed: {
    ...mapGetters([
      'user'
    ]),
    getUser () {
      if (!this.user) {
        return 'no user'
      } else {
        return this.user
      }
    }
  },
  data () {
    return {
      valid: false,
      userName: '',
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required'
      ],
      userRules: [
        v => {
          return !!v || 'User is required'
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
