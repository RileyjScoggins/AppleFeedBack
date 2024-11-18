# List of comments (with some duplicates)
comments = [
    "The immersive experience of the Apple Vision Pro is unlike anything I've tried before. However, the battery life doesn't last as long as I'd hoped, requiring frequent charging throughout the day.",
    "I love the sleek design of the Vision Pro, and it fits comfortably even during extended use. The materials feel premium, and it definitely turns heads.",
    "The price tag of the Vision Pro is quite steep, making it hard to justify the investment for the average user. I wish there were a more affordable option with similar features.",
    "Navigating through the interface feels intuitive, and the integration with other Apple devices is seamless. It's great how easily it syncs with my iPhone and MacBook.",
    "I experienced some lag while running high-demand applications, which was disappointing for such a premium product. It interrupted my workflow and was quite frustrating.",
    "Customer service was incredibly helpful when I had trouble setting up the Vision Pro for the first time. They walked me through each step patiently until everything was working smoothly.",
    "The Vision Pro's augmented reality features are impressive, bringing digital elements into the real world convincingly. However, the selection of compatible apps is still limited, which reduces its utility.",
    "Wearing the headset for more than two hours becomes uncomfortable, as it puts pressure on my nose. I hope future versions will address the weight distribution better.",
    "I appreciate the high-quality build and materials used in the Vision Pro; it feels durable and premium. The attention to detail in its design is truly remarkable.",
    "The setup process was a bit complicated and not as straightforward as other Apple products I've used. It took me a while to figure out the calibration settings.",
    "The battery life is exceptional, allowing me to use the Vision Pro throughout the day without needing a recharge. This is perfect for long work sessions or extended entertainment.",
    "I wish the Vision Pro was lighter; after a while, it starts to feel cumbersome. It's not ideal for long-term wear, especially during travel.",
    "The display resolution is stunning, making every detail crisp and clear. Watching movies and viewing photos is an entirely new experience with this level of clarity.",
    "I'm impressed with how smoothly the Vision Pro runs even the most demanding applications. Multitasking is a breeze, and I haven't encountered any performance issues.",
    "I encountered some software glitches that required restarting the device, which interrupted my work. For the price, I expected a more stable software experience.",
    "The Vision Pro seamlessly syncs with my Mac and iPhone, enhancing my productivity. The continuity between devices makes it easy to pick up where I left off.",
    "Considering its features, the Vision Pro offers good value for the money. It's an investment, but the functionality it provides justifies the cost for me.",
    "I was underwhelmed by the limited customization options available in the settings. I'd like more control over the user interface and features.",
    "The audio quality is immersive, making media consumption a joy on the Vision Pro. The spatial audio adds depth to movies and music that I've never experienced before.",
    "It's frustrating that some essential apps are not yet optimized for the Vision Pro. This limits its usefulness for my daily tasks.",
    "The Vision Pro's display is incredibly sharp, and the color accuracy is top-notch, making it perfect for creative work. However, I noticed some minor overheating during extended sessions.",
    "I love how easy it is to switch between AR and VR modes. It feels natural and enhances productivity, but the learning curve for certain gestures was steeper than I expected.",
    "The headset is a game-changer for virtual meetings, making interactions feel much more personal. However, the price point makes it hard to recommend to everyone on my team.",
    "The build quality is excellent, but I wish the device had more padding around the face for added comfort. After a few hours, it starts to feel a bit tight.",
    "The Vision Pro integrates perfectly with Apple services like iCloud and FaceTime. It's nice to see everything work together so seamlessly, as expected from Apple.",
    "While the design is futuristic and sleek, the lack of adjustable straps for head sizes was a bit inconvenient. It took me a while to get a snug fit.",
    "The Vision Pro's audio system is phenomenal, providing an immersive experience without the need for headphones. It’s one of the standout features for me.",
    # ... more comments
]

# Remove duplicates by converting the list to a set and then back to a list
unique_comments = list(set(comments))

# Optionally, sort the comments if you want them in a specific order
unique_comments.sort()

# Print the cleaned list
for comment in unique_comments:
    print(comment)
