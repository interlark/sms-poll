import {
  Spinner,
  VStack,
  Progress,
  useInterval,
  Flex,
  HStack,
  Box,
  useColorMode,
  Image,
  Text,
  StackDivider,
  useBreakpointValue,
} from "@chakra-ui/react"
import { Fragment, useEffect, useState } from "react"
import axios from "axios"
import img_empty_dark from "../../images/empty_list_dark.png"
import img_empty_light from "../../images/empty_list_light.png"

function App() {
  const initState = {
    strings: {'#': '#', 'Item': 'Item', 'Votes': 'Votes', 'Phone': '(123) 456-7890'},
    items: [],
    loading: true,
  }
  const [state, setState] = useState(initState)
  const { colorMode, setColorMode } = useColorMode()

  const getStrings = async () => {
    const res = await axios.get("/settings/strings")
    return Object.assign({}, ...res.data.map(x => ({[x.name]: x.value})))
  }

  const getItems = async () => {
    const res = await axios.get("/items/")
    return res.data.slice(0,50)
  }

  const getTheme = async () => {
    const res = await axios.get('/settings/flags/light_theme_poll')
    return res.data.value ? "light" : "dark"
  }

  useEffect(() => {
    const fetchData = async() => {
      try {
        const theme = await getTheme()
        setColorMode(theme)

        const strings = await getStrings()
        const items = await getItems()
        setState({...state, strings, items, phone, loading: false})
      } catch (error) {
        setState({...state, loading: false})
        console.error(error)
      }
    }
    fetchData()
  }, [])

  useInterval(async () => {
    if (!state.loading){
      const items = await getItems()
      setState({...state, items})
    }
  }, 3000)

  const getDividerStyle = ({isBold}) => {
    return {
      sx: {
        "&&": {
            borderColor: isBold ? "white" : "inherit",
            my: "0.3rem",
            mx: 0,
            borderLeftWidth: 0,
            borderBottomWidth: "1px",
        }
      }
    }
  }

  const getRowStyle = () => {
    return {
      sx: {
        "&&": {
            my: "0",
        }
      }
    }
  }

  const {strings, phone, items, loading} = state
  const textFontSize = useBreakpointValue({ base: 12, sm: 21, md: 27, lg: 32, xl: 35 })

  if (loading) {
    return (
      <VStack minH="100vh" justifyContent="center">
        <Spinner size="xl" />
      </VStack>
    )
  }

  if (!items.length) {
    const img_empty = colorMode === "light" ? img_empty_light : img_empty_dark
  
    return (
      <Flex w="100vw" h="100vh" justifyContent="center" alignItems="center">
          <Image
            src={img_empty}
            alt="Your items list is empty!"
          />
      </Flex>
    )
  }

  // const totalNumberOfVotes = items.reduce((acc, obj) => acc + obj.votes_count, 0) 
  const maxNumberOfVotes = items.reduce((acc, obj) => acc > obj.votes_count ? acc : obj.votes_count, 1)

  return (
    <VStack p={4} h="100vh" m="0 auto">
      <VStack
        h="100vh" w="95vw"
        flex="1" overflowY="auto"
        fontSize={textFontSize}
      >
        <HStack w="100%" flexBasis={`${textFontSize * 3.5}px`} fontWeight={700} {...getRowStyle()}>
          <Box flex="1 0 10vw">{strings["#"]}</Box>
          <Box flex="1 0 30vw">{strings["Item"]}</Box>
          <Flex justifyContent="center" flex="1 0 10vw">{strings["Votes"]}</Flex>
          <Box flex="1 0 30vw"></Box>
        </HStack>

        <StackDivider {...getDividerStyle({isBold: true})} />

        {items.map((item, idx, arr) => (
          <Fragment>
            <HStack w="100%" flexBasis={`${textFontSize * 3.5}px`} key={item.id} {...getRowStyle()}>
              <Box flex="1 0 10vw" fontWeight={700}>{item.id}</Box>
              <Box flex="1 0 30vw">{item.name}</Box>
              <Flex justifyContent="center" flex="1 0 10vw">{item.votes_count}</Flex>
              <Box flex="1 0 30vw">
                <Progress
                  colorScheme="gray"
                  h={`${textFontSize}px`}
                  ml="1.5vw"
                  sx={{
                    "& > div:first-of-type": {
                      transitionProperty: "width",
                    },
                  }}
                  value={item.votes_count / maxNumberOfVotes * 100}
                />
              </Box>
            </HStack>
            <StackDivider {...getDividerStyle({isBold: idx == arr.length - 1})} />
          </Fragment>
          ))}
      </VStack>
      <VStack
        h="100vh" w="95vw"
        fontSize={`${textFontSize * 2.25}px`}
        flex="1" flexGrow="0"
        alignItems="center" justifyContent="center"
      >
        <Text>{strings["Phone"]}</Text>
      </VStack>
    </VStack>
  )
}

export default App
