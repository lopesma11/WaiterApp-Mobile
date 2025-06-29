import styled from "styled-components/native";
import { Platform, StatusBar } from "react-native";

const isAndroid = Platform.OS === "android";

console.log({ isAndroid, currentHeight: StatusBar.currentHeight });

export const Container = styled.SafeAreaView`
    margin-top: ${isAndroid ? `${StatusBar.currentHeight}px` : "0"};
    background: #fafafa;
    flex: 1;
`;

export const CategoriesContainer = styled.View`
    height: 146px;
    background: #fff;
    margin-top: 34px;
`;

export const MenuContainer = styled.View`
    flex: 1;
    background: #fff;
`;

export const Footer = styled.View`
    min-height: 110px;
    background: #fff;
    padding: 16px 24px;
`;

export const FooterContainer = styled.SafeAreaView``;
