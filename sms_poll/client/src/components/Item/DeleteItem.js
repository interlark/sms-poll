import {
  Button,
  IconButton,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Text,
  useDisclosure,
} from "@chakra-ui/react"
import { Fragment } from "react"
import { FiTrash2 } from "react-icons/fi"

function DeleteAllItems({ deleteItemsAll }) {
  const { isOpen, onOpen, onClose } = useDisclosure()
  return (
    <Fragment>
      <Button
        colorScheme="gray"
        px="8"
        h="45"
        color="gray.500"
        mt="8"
        onClick={onOpen}
      >
        Delete all items
      </Button>

      <Modal isCentered isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent w="90%">
          <ModalHeader>
            Are you sure you want to delete all items?
          </ModalHeader>
          <ModalFooter>
            <Button mr={3} onClick={onClose}>
              Cancel
            </Button>
            <Button colorScheme="red" onClick={() => deleteItemsAll()}>
              Delete
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Fragment>
  )
}

function DeleteItem({ item, deleteItem }) {
  const { isOpen, onOpen, onClose } = useDisclosure()

  return (
    <Fragment>
      <IconButton icon={<FiTrash2 />} isRound="true" onClick={onOpen} />

      <Modal isCentered isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent w="90%">
          <ModalHeader>
            Are you sure you want to delete this item?
          </ModalHeader>
          <ModalBody>
            <Text>{item.name}</Text>
          </ModalBody>
          <ModalFooter>
            <Button mr={3} onClick={onClose}>
              Cancel
            </Button>
            <Button
              colorScheme="red"
              onClick={() => deleteItem(item.id, onClose)}
            >
              Delete
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Fragment>
  )
}

export { DeleteItem, DeleteAllItems }
