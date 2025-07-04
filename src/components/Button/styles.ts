import styled from "styled-components/native";

export const Container = styled.TouchableOpacity`
    background: ${({ disabled }) => (disabled ? "#999" : "#000000")};
    border-radius: 48px;
    padding: 14px 24px;
    align-items: center;
    justify-content: center;
`;
