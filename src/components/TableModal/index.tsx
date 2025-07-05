import { Modal, Platform, TouchableOpacity } from "react-native";
import { Text } from "../Text";
import { Overlay, ModalBody, Header, Form, Input } from "./styles";
import { Close } from "../Icons/Close";
import { Button } from "../Button";
import { useState } from "react";

interface TableModalProps {
    visible: boolean;
    onClose: () => void;
    onSave: (table: string) => void;
}

export function TableModal({ visible, onClose, onSave }: TableModalProps) {
    const [table, setTable] = useState<string>("");

    function handleSave() {
        setTable("");
        onSave(table);
        onClose();
    }

    return (
        <Modal visible={visible} transparent animationType="fade">
            <Overlay
                behavior={Platform.OS === "android" ? "height" : "padding"}
            >
                <ModalBody>
                    <Header>
                        <Text weight="600">Informe a mesa</Text>

                        <TouchableOpacity onPress={onClose}>
                            <Close color="#000" />
                        </TouchableOpacity>
                    </Header>
                    <Form>
                        <Input
                            placeholder="Número da mesa"
                            placeholderTextColor="#666"
                            keyboardType="number-pad"
                            onChangeText={setTable}
                        ></Input>
                        <Button
                            onPress={handleSave}
                            disabled={table.length === 0}
                        >
                            Salvar
                        </Button>
                    </Form>
                </ModalBody>
            </Overlay>
        </Modal>
    );
}
