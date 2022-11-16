import axios from 'axios'

const login = {
  namespaced: true,
  state: {
    token: null,
    username: null,
    imgUrl: null,
  },
  getters: {
    username(state) { return state.username}
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    KAKAO_SAVE(state, payload) {
      state.username = payload.username
      state.imgUrl = payload.imgUrl
    }
  },
  actions: {
    login({commit}, payload) {
      console.log(payload)
      axios({
        url: 'http://127.0.0.1:8000/accounts/login/',
        method: 'post',
        data: payload
      })
        .then(res => {
          const token = res.data.key
          commit('SAVE_TOKEN', token)
          alert('로그인 성공!')
          // router 등록하기
        })
        .catch(err => {
          alert('잘못 입력하셨습니다.', err) // json stringfy로 에러 출력하기
        })
    },
    kakaoLogin({commit}) {
      window.Kakao.init('39caf5e8e7fed0bce24af6168049aae6')
      window.Kakao.Auth.login({
        scope: 'account_email, profile_image',
        success: (res) => {
          console.log(res)
          window.Kakao.API.request({
            url: '/v2/user/me',
            success: (res) => {
              console.log(res, 'hi')
              const username = res.kakao_account.email
              const imgUrl = res.kakao_account.profile.profile_image_url
              commit('KAKAO_SAVE', {username, imgUrl})
              // this.$router.push({name : 'SignUpView'})
            },
            fail: (err) => {
              console.log(err)
            }
          })
        }
      })
    },
    signUp(context, password) { //400 은 이미 가입한 아이디
      axios({
        url: 'http://127.0.0.1:8000/accounts/signup',
        method: 'post',
        data: {
          username: context.state.username, // 또는 매개변수로 전달받아서 사용
          password1: password.password1,
          password2: password.password2,
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
    }
  }
}

export default login

