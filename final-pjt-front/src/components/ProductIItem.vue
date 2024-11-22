<template>
    <div class="main-content">
        <div class="product-content">
            <p class = indexnum>{{ index+1 }} /</p>
            <img :src="getBankLogo(myProduct.product.company_name)" :alt="myProduct.product.company_name" class="bank-logo">
        </div>
        <div class="product">
            <div class="product-duration">
                <p class="bankname">{{ myProduct.product.company_name}}</p>
                <span>{{ myProduct.product.product_name}}</span>
                <div class="duration-section">
                    <p>가입일: {{ myProduct.join_date.slice(0,10) }}</p>
                    <p>만기일: {{ myProduct.expiration_date.slice(0,10) }} <span>(D-{{myProduct.d_day}})</span></p> 
                </div>
            </div>
            <div class="monthly-amount">
                <span>적용 금리: {{ myProduct.interest_rate }}%</span>
                <p class="monthly">월 납입액: {{ (myProduct.monthly_amount*10000).toLocaleString(en-US)}}원</p>
                <p class="amount">{{ (myProduct.remain_month*myProduct.monthly_amount*10000).toLocaleString(en-US) }}원</p>
            </div>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    myProduct:Object,
    index:Number
})


// const getBankLogo = (categoryName) => {
//     const bankName = categoryName.split(' > ').pop();
//     const bankLogos = {
//       'KB국민은행': require('@/assets/images/kb.png'),
//         '신한은행': require('@/assets/images/shinhan.png'),
//         '하나은행': require('@/assets/images/hana.png'),
//         '우리은행': require('@/assets/images/woori.png'),
//         'NH농협은행': require('@/assets/images/nh.png'),
//         'IBK기업은행': require('@/assets/images/IBK.png'),
//         'KDB산업은행': require('@/assets/images/KDB.png'),
//         'SC제일은행': require('@/assets/images/sc.png'),
//         '부산은행': require('@/assets/images/BUSAN.png'),
//         'iM뱅크': require('@/assets/images/IM.png'),
//         'SH수협은행': require('@/assets/images/SH.png'),
//         '경남은행': require('@/assets/images/BUSAN.png'),
//         '카카오뱅크': require('@/assets/images/kakao.png'),
//         '광주은행': require('@/assets/images/KWANGJU.png'),
//         '토스뱅크': require('@/assets/images/toss.png'),
//         '전북은행': require('@/assets/images/JEONBUK.png'),
//         '케이뱅크': require('@/assets/images/kbank.png'),
//         '제주은행': require('@/assets/images/shinhan.png'),
//     };
//     return bankLogos[bankName] || require('@/assets/images/default.png');
// };

import kbLogo from '@/assets/images/kb.png';
import shinhanLogo from '@/assets/images/shinhan.png';
import hanaLogo from '@/assets/images/hana.png';
import wooriLogo from '@/assets/images/woori.png';
import nhLogo from '@/assets/images/nh.png';
import ibkLogo from '@/assets/images/IBK.png';
import kdbLogo from '@/assets/images/KDB.png';
import scLogo from '@/assets/images/sc.png';
import busanLogo from '@/assets/images/BUSAN.png';
import imBankLogo from '@/assets/images/IM.png';
import shLogo from '@/assets/images/SH.png';
import kakaoLogo from '@/assets/images/kakao.png';
import kwangjuLogo from '@/assets/images/KWANGJU.png';
import tossLogo from '@/assets/images/toss.png';
import jeonbukLogo from '@/assets/images/JEONBUK.png';
import kbankLogo from '@/assets/images/kbank.png';

// 기본 로고 (없을 경우 표시)
const defaultLogo = '/images/default.png';

// 은행 로고 매핑
const bankLogos = {
  'KB국민은행': kbLogo,
  '신한은행': shinhanLogo,
  '제주은행': shinhanLogo,
  '하나은행': hanaLogo,
  '우리은행': wooriLogo,
  'NH농협은행': nhLogo,
  'IBK기업은행': ibkLogo,
  'KDB산업은행': kdbLogo,
  'SC제일은행': scLogo,
  '부산은행': busanLogo,
  '경남은행': busanLogo,
  'iM뱅크': imBankLogo,
  'SH수협은행': shLogo,
  '카카오뱅크': kakaoLogo,
  '광주은행': kwangjuLogo,
  '토스뱅크': tossLogo,
  '전북은행': jeonbukLogo,
  '케이뱅크': kbankLogo,
};

// 로고 반환 함수
const getBankLogo = (categoryName) => {
  const bankName = categoryName.split(' > ').pop(); // 이름에서 마지막 값 추출
  return bankLogos[bankName] || defaultLogo; // 해당 로고가 없으면 기본 로고 반환
};

</script>

<style scoped>

.main-content {
    display: flex;
    margin: 10px 0;
    border-bottom: 1px solid #BCBCBC;
    padding-bottom: 25px;
}

.product-content {
    display: flex;
}

.indexnum {
    font-size: larger;
}

.bank-logo {
    width: 35px;
    height: 35px;
    margin-left: 15px;
    margin-top: 5px;
}

.product {
    display: flex;
    justify-content: space-between;
    flex-grow: 2;
    
}

.product-duration {
    margin-left: 30px;
}

.product-duration > .bankname {
    color: #808080;
}

.product-duration > span {
    font-size: 18px;
    font-weight: 700;
}

.product-content {
    color: #FFA46B;
    font-size: 22px;
}

.duration-section > p {
    color: #BCBCBC;
    font-weight: 300;
}

.duration-section > p > span {
    color: #FFAE17;
}

.monthly-amount {
    align-self: end;
    text-align: end;
    margin-top: 73px;
}

.monthly-amount > span {
    color: #BCBCBC;
    font-weight: 300;
}

.monthly-amount > .monthly {
    color: #808080;
    font-weight: 700;
}

.monthly-amount > .amount {
    font-size: 20px;
    color: #FFA46B;
    font-weight: 700;

}

</style>