import {
  Box,
  Button,
  Flex,
  HStack,
  Image,
  StackDivider,
  Text,
  useColorMode,
  VStack,
} from "@chakra-ui/react"
import { Fragment } from "react"
import img_empty_dark from "../../images/empty_list_dark.png"
import img_empty_light from "../../images/empty_list_light.png"
import { DeleteAllItems, DeleteItem } from "./DeleteItem"
import UpdateItem from "./UpdateItem"

function ItemList({ items, updateItem, deleteItem, deleteItemsAll }) {
  const { colorMode } = useColorMode()
  const img_empty = colorMode === "light" ? img_empty_light : img_empty_dark

  if (!items.length) {
    return (
      <Box maxW="80%">
        <Image
          mt="20px"
          w="98%"
          maxW="350"
          src={img_empty}
          alt="Your items list is empty!"
        />
      </Box>
    )
  }

  return (
    <Fragment>
      <VStack
        divider={<StackDivider />}
        borderColor="gray.100"
        borderWidth="2px"
        p="5"
        borderRadius="lg"
        w="100%"
        alignItems="stretch"
      >
        {items.map((item) => (
          <HStack key={item.id}>
            <Button as="div" cursor="default" size="sm">
              {item.id}
            </Button>
            <Text w="100%" p="8px" borderRadius="lg">
              {item.name}
            </Text>
            <DeleteItem
              item={item}
              deleteItem={deleteItem}
              deleteItemsAll={deleteItemsAll}
            />
            <UpdateItem item={item} updateItem={updateItem} />
          </HStack>
        ))}
      </VStack>

      <Flex>
        <DeleteAllItems deleteItemsAll={deleteItemsAll} />
      </Flex>
    </Fragment>
  )
}

export default ItemList
