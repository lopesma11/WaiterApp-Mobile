import { FlatList } from "react-native";

import { products } from "../../mocks/products";
import { Text } from "../Text";
import {
    Product,
    ProductImage,
    ProductDetails,
    Separator,
    AddToCartButton,
} from "./styles";
import { formatCurrency } from "../../utils/formatCurrency";
import { PlusCircle } from "../Icons/PlusCircle";

export function Menu() {
    function getImageUri(imagePath: string) {
        const baseUrl = "http://192.168.0.15:3001";
        return `${baseUrl}/uploads/${imagePath}`;
    }
    return (
        <FlatList
            data={products}
            style={{ marginTop: 32 }}
            contentContainerStyle={{ paddingHorizontal: 24 }}
            keyExtractor={(product) => product._id}
            ItemSeparatorComponent={Separator}
            renderItem={({ item: product }) => (
                <Product>
                    <ProductImage
                        source={{
                            uri: `http://192.168.0.15:3001/uploads/${product.imagePath}`,
                        }}
                    />

                    {/* <ProductImage
                        source={{
                            uri: getImageUri(product.imagePath),
                        }}
                        // Adicionar props para debug e fallback
                        onError={(error: any) => {
                            console.log(
                                "Erro ao carregar imagem:",
                                error.nativeEvent.error
                            );
                        }}
                        onLoad={() => {
                            console.log(
                                "Imagem carregada com sucesso:",
                                product.name
                            );
                        }}
                        // Adicionar resizeMode para melhor exibição
                        resizeMode="cover"
                    /> */}

                    <ProductDetails>
                        <Text weight="600">{product.name}</Text>
                        <Text
                            size={14}
                            color="#666"
                            style={{ marginVertical: 8 }}
                        >
                            {product.description}
                        </Text>
                        <Text size={14} weight="600">
                            {formatCurrency(product.price)}
                        </Text>
                    </ProductDetails>

                    <AddToCartButton>
                        <PlusCircle />
                    </AddToCartButton>
                </Product>
            )}
        />
    );
}
