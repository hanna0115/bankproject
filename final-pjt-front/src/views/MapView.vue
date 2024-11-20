<template>
    <div class="container">
      <div class="content">
        <h2 class="title">지도</h2>
        <div class="select-container">
          <select v-model="selectedCity" @change="handleCityChange" class="select-box">
            <option value="">광역시/도</option>
            <option v-for="city in cities" :key="city.name" :value="city">
              {{ city.name }}
            </option>
          </select>
          <select v-model="selectedDistrict" @change="handleDistrictChange" class="select-box" :disabled="!selectedCity">
            <option value="">시/군/구</option>
            <option v-for="district in filteredDistricts" :key="district" :value="district">
              {{ district }}
            </option>
          </select>
          <select v-model="selectedBank" @change="handleBankChange" class="select-box">
            <option value="">은행</option>
            <option v-for="bank in banks" :key="bank" :value="bank">
              {{ bank }}
            </option>
          </select>
        </div>
        <div class="map-container">
          <div class="kakaomap">
            <KakaoMap :lat="36.353705" :lng="127.341557" @onLoadKakaoMap="onLoadKakaoMap" width="100%">
              <KakaoMapMarker 
                v-for="(marker, index) in markerList" 
                :key="index"
                :lat="marker.lat"
                :lng="marker.lng"
                :infoWindow="marker.infoWindow"
                :clickable="true"
                @onClickKakaoMapMarker="onClickMapMarker(marker)"
              />
            </KakaoMap>
          </div>
          <div class="place-list">
            <div class="place-item" v-for="(place, index) in placeList" :key="index" @click="moveToMarker(place)">
              <div class="bank-info">
                <img :src="getBankLogo(place.category_name)" alt="bank-logo" class="bank-logo">
                <div class="bank-details">
                  <h5>{{ place.place_name }}</h5>
                  <div></div>
                  <p>{{ place.address_name }}</p>
                  <p>{{ place.phone }}</p>
                  <p>평일 09:00 - 18:00</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, watch, onMounted } from 'vue'
  import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
  
  const map = ref();
  const markerList = ref([]);
  const placeList = ref([]);
  
  const searchKeyword = computed(() => {
    let keyword = '';
    if (selectedCity.value) {
      keyword += selectedCity.value.name;
      if (selectedDistrict.value) {
        keyword += ' ' + selectedDistrict.value;
      }
    }
    if (selectedBank.value) {
      keyword += ' ' + selectedBank.value;
    }
    return keyword;
  });
  
  const onLoadKakaoMap = (mapRef) => {
    map.value = mapRef;
    searchPlaces();
  };
  
  const searchPlaces = () => {
    if (!map.value) return;
    markerList.value = [];
    const ps = new kakao.maps.services.Places();
    if (searchKeyword.value) {
      ps.keywordSearch(searchKeyword.value, placesSearchCB);
    }
  };
  
  const placesSearchCB = (data, status) => {
    if (status === kakao.maps.services.Status.OK) {
      const bounds = new kakao.maps.LatLngBounds();
      placeList.value = data;
      console.log(placeList)
      markerList.value = data.map(marker => ({
        lat: marker.y,
        lng: marker.x,
        infoWindow: {
          content: `
            <div style="padding:5px;font-size:12px;">
              ${marker.place_name}<br>
              ${marker.address_name}<br>
              ${marker.phone}
            </div>
          `,
          visible: false
        }
      }));
      markerList.value.forEach(marker => {
        bounds.extend(new kakao.maps.LatLng(Number(marker.lat), Number(marker.lng)));
      });
      map.value?.setBounds(bounds);
    }
  };
  
  const moveToMarker = (place) => {
    const moveLatLng = new kakao.maps.LatLng(place.y, place.x);
    map.value?.setCenter(moveLatLng);
    map.value?.setLevel(3);
  };
  
  const onClickMapMarker = (markerItem) => {
    if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
      markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
    } else {
      markerItem.infoWindow.visible = true;
    }
  };
  
  const getBankLogo = (categoryName) => {
    const bankName = categoryName.split(' > ').pop();
    const bankLogos = {
      'KB국민은행': 'src/assets/images/kb.png',
      '신한은행': 'src/assets/images/shinhan.png',
      '우리은행': 'src/assets/images/woori.png',
      'NH농협은행': 'src/assets/images/nh.png',
      '하나은행': 'src/assets/images/hana.png',
      'IBK기업은행': 'src/assets/images/ibk.png',
      'SC제일은행': 'src/assets/images/sc.png',
      '씨티은행': 'src/assets/images/citi.png',
      'KDB산업은행': 'src/assets/images/kdb.png',
      '카카오뱅크': 'src/assets/images/kakao.png',
      '토스뱅크': 'src/assets/images/toss.png',
      'K뱅크': 'src/assets/images/kbank.png',
      'ATM': 'src/assets/images/bankproject.png'
    };
    return bankLogos[bankName] || '/images/default.png';
  };
  
  const cities = [
  {
    name: '서울특별시',
    districts: ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
  },
  {
    name: '부산광역시', 
    districts: ['강서구', '금정구', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구']
  },
  {
    name: '대구광역시',
    districts: ['남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구']
  },
  {
    name: '인천광역시',
    districts: ['계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '중구', '강화군', '옹진군']
  },
  {
    name: '광주광역시',
    districts: ['광산구', '남구', '동구', '북구', '서구']
  },
  {
    name: '대전광역시',
    districts: ['대덕구', '동구', '서구', '유성구', '중구']
  },
  {
    name: '울산광역시',
    districts: ['남구', '동구', '북구', '중구', '울주군']
  },
  {
    name: '세종특별자치시',
    districts: ['세종시']
  },
  {
    name: '경기도',
    districts: ['고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시', '가평군', '양평군', '여주시', '연천군']
  },
  {
    name: '강원도',
    districts: ['강릉시', '동해시', '삼척시', '속초시', '원주시', '춘천시', '태백시', '고성군', '양구군', '양양군', '영월군', '인제군', '정선군', '철원군', '평창군', '홍천군', '화천군', '횡성군']
  },
  {
    name: '충청북도',
    districts: ['제천시', '청주시', '충주시', '괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '증평군', '진천군']
  },
  {
    name: '충청남도',
    districts: ['계룡시', '공주시', '논산시', '당진시', '보령시', '서산시', '아산시', '천안시', '금산군', '부여군', '서천군', '예산군', '청양군', '태안군', '홍성군']
  },
  {
    name: '전라북도',
    districts: ['군산시', '김제시', '남원시', '익산시', '전주시', '정읍시', '고창군', '무주군', '부안군', '순창군', '완주군', '임실군', '장수군', '진안군']
  },
  {
    name: '전라남도',
    districts: ['광양시', '나주시', '목포시', '순천시', '여수시', '강진군', '고흥군', '곡성군', '구례군', '담양군', '무안군', '보성군', '신안군', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군']
  },
  {
    name: '경상북도',
    districts: ['경산시', '경주시', '구미시', '김천시', '문경시', '상주시', '안동시', '영주시', '영천시', '포항시', '고령군', '군위군', '봉화군', '성주군', '영덕군', '영양군', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군']
  },
  {
    name: '경상남도',
    districts: ['거제시', '김해시', '밀양시', '사천시', '양산시', '진주시', '창원시', '통영시', '거창군', '고성군', '남해군', '산청군', '의령군', '창녕군', '하동군', '함안군', '함양군', '합천군']
  },
  {
    name: '제주특별자치도',
    districts: ['제주시', '서귀포시']
  }
];
  
  const banks = [
    'KB국민은행', '신한은행', '우리은행', 'NH농협은행', '하나은행', 
    'IBK기업은행', 'SC제일은행', '씨티은행', 'KDB산업은행', 
    '카카오뱅크', '토스뱅크', 'K뱅크'
  ];
  
  const selectedCity = ref({
    name: '대전광역시',
    districts: ['대덕구', '동구', '서구', '유성구', '중구']
  });
  const selectedDistrict = ref('유성구');
  const selectedBank = ref('KB국민은행');
  
  const filteredDistricts = computed(() => {
    if (!selectedCity.value) return [];
    return selectedCity.value.districts || [];
  });
  
  const handleCityChange = () => {
    selectedDistrict.value = '';
    searchPlaces();
  };
  
  const handleDistrictChange = () => {
    searchPlaces();
  };
  
  const handleBankChange = () => {
    searchPlaces();
  };
  
  watch([selectedCity, selectedDistrict, selectedBank], () => {
    searchPlaces();
  });
  
  onMounted(() => {
    searchPlaces();
  });
  </script>
  
  <style scoped>
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 100px auto 0px;
    width: 1280px;
  }
  
  .content {
    width: 80%;
  }
  
  .title {
    display: flex;
    justify-content: center;
    align-content: center;
    color: #FF6708;
  }
  
  .select-container {
    display: flex;
    position: relative;
    gap: 10px;
    margin-top: 70px;
  }
  
  .select-box {
    padding: 8px 12px;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
    font-size: 14px;
    min-width: 150px;
    background-color: white;
    cursor: pointer;
  }
  
  .select-box:disabled {
    background-color: #f5f5f5;
    cursor: not-allowed;
  }
  
  .select-box:focus {
    outline: none;
    border-color: #FF6708;
  }
  
  .select-box option {
    padding: 8px;
  }
  
  .map-container {
    display: flex;
    gap: 20px;
    margin-top: 20px;
  }
  
  .kakaomap {
    flex: 1;
    height: 600px;
  }
  
  .place-list {
    width: 300px;
    overflow-y: auto;
    max-height: 600px;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
    height: 480px;
  }
  
  .place-item {
    padding: 15px;
    border-bottom: 1px solid #E5E5E5;
    cursor: pointer;
  }
  
  .place-item:hover {
    background-color: #f5f5f5;
  }
  
  .bank-info {
    display: flex;
    gap: 10px;
  }
  
  .bank-logo {
    width: 40px;
    height: 40px;
    object-fit: contain;
  }
  
  .bank-details h3 {
    margin: 0 0 5px 0;
    font-size: 16px;
  }
  
  .bank-details p {
    margin: 3px 0;
    font-size: 14px;
    color: #666;
  }
  </style>