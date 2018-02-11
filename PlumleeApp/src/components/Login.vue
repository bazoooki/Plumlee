<template>
  <v-layout row wrap justify-center align-center>
    <v-flex xs12 md5 text-xs-center>
      <v-card class="pa-3">
        <h2 class="green--text darken-1">Login to plumlee</h2>
        <v-layout row wrap justify-center>
          <v-flex xs10 md10>
            <v-form v-model="valid" ref="form" lazy-validation>    
              <v-text-field label="User" v-model="user" :rules="userRules" required></v-text-field>
              <v-text-field label="Password" type="password" name="password" v-model="password" :rules="passwordRules" required></v-text-field>
               <v-btn @click="submit" :disabled="!valid" color="primary">Login</v-btn>               
            </v-form>
          </v-flex>
        </v-layout>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'Login',
  methods: {
    ...mapActions([
      'login',
      'whoami'
    ]),
    submit () {
      this.login({user: this.user, password: this.password}).then((res) => {
        if (res.data.status === 0) {
          console.log('Sorry user doesnt exists')
        } else {
          this.$router.push({name: 'Home', params: { userId: 123 }})
        }
      })
    },
    clear () {
      this.$refs.form.reset()
    }
  },
  computed: {
  },
  data () {
    return {
      valid: false,
      user: '',
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
