import axios from 'axios'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

const login = {
  namespaced: true,
  state: {
    token: null,
    user: null,
    profile: null,
  },
  getters: {
    user: (state) => state.user,
    authHead: (state) => ({Authorization: `Token ${state.token}`}),
    isLogin: (state) => state.token ? true : false,
    profile: (state) => state.profile
  },
  mutations: {
    SAVE_TOKEN: (state, token) => state.token = token,
    SET_USER: (state, user) => state.user = user,
    PROFILE_INFO: (state, profile) => state.profile = profile
  },
  actions: {
    login({commit, dispatch}, payload) {
      axios({
        url: `${API_URL}/accounts/login/`,
        method: 'post',
        data: payload
      })
        .then(res => {
          const token = res.data.key
          commit('SAVE_TOKEN', token)
          dispatch('getUserInfo')
          alert('로그인 성공!')
          router.push('/') // app 창으로 이동
        })
        .catch(err => {
          alert('잘못 입력하셨습니다.', err) // json stringfy로 에러 출력하기
        })
    },
    getUserInfo({commit, getters}) {
      axios({
        url: `${API_URL}/accounts/user/`,
        method: 'get',
        headers: getters.authHead,
      })
        .then(res => {
          commit('SET_USER', res.data)
        })
        //https://stackoverflow.com/questions/70198922/user-profile-update-using-dj-rest-auth-allauth > userinfo custom
    },   
    signUpAction({commit, dispatch}, formData) { //400 은 이미 가입한 아이디
        axios({
          headers: {
            "Content-Type": "multipart/form-data",
          },
          url: `${API_URL}/accounts/signup/`,
          method: 'post',
          data: formData
        })
          .then(res => {
            commit('SAVE_TOKEN', res.data.key)
            dispatch('getUserInfo')
            alert('가입 성공!')
            router.push('/') // app 창으로 이동
          })
    },
    logout( {commit, getters} ) { // contect 안에 commit과 getters이 포함되어 있으니까 중괄호로 같이 묶어야함
      axios({
        url: `${API_URL}/accounts/logout/`,
        method: 'post',
        headers: getters.authHead
      })
        .then(res => {
          console.log(res)
          commit('SAVE_TOKEN', null)
          commit('SET_USER', null) //유저와 token 초기화
          router.push('/')
        })
        .catch(err => {
          console.log(err)
        })
    },
    profileInfo({commit, getters}, user_pk){
      axios({
        url: `${API_URL}/user/profile/${user_pk}/`,
        method: 'get',
        headers: getters.authHead,
      })
        .then(res => {
          commit('PROFILE_INFO', res.data)
        })
    },
    fixFollower({dispatch, getters}, pk) {
      axios({
        url: `${API_URL}/user/follow/`,
        method: 'post',
        headers: getters.authHead,
        data: {
          "user_pk": pk
        }
      })
        .then(res => {
          console.log(res)
          dispatch('profileInfo', pk)
        })      
    }

    // kakaoLogin({commit}) {
    //   window.Kakao.init('39caf5e8e7fed0bce24af6168049aae6')
    //   window.Kakao.Auth.login({
    //     scope: 'account_email, profile_image',
    //     success: (res) => {
    //       console.log(res)
    //       window.Kakao.API.request({
    //         url: '/v2/user/me',
    //         success: (res) => {
    //           console.log(res, 'hi')
    //           const username = res.kakao_account.email
    //           const imgUrl = res.kakao_account.profile.profile_image_url
    //           commit('KAKAO_SAVE', {username, imgUrl})
    //           // this.$router.push({name : 'SignUpView'})
    //         },
    //         fail: (err) => {
    //           console.log(err)
    //         }
    //       })
    //     }
    //   })
    // },
  }
}

export default login

