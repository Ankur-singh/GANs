# GANs

I recently stared reading about GANs. I must admit, its quite an interesting field with applications in numerous fields. Quickly I was overwhelmed by all the blogs, videos, and research papers. So, I decided to approach the topics in an organized manner and document everything in the process. Hence this repo . . .

I watched several video on YouTube, read a few blogs & also tried reading some research papers. But if you are just starting with GANs, I will suggest that you start with the following resourses. This will help you maintain your sanity.

## Resources

1. [Introduction to GANs by Ian Goodfellow](https://youtu.be/RvgYvHyT15E), this talk is very insightfull and deserves to be watched multiple times. Here are some of the important take away:
    - In normal Machine Learning or Deep Learning, we only have one differentiable network and one loss function that we optimize for. But in Adversarial training, we have two differentiable networks, each with different loss function. Its called Adversarial training because worst case output for one network is produced by another network. And since both the agents are Neural Networks & are used for generating data, its called GANs (Generative Adversarial Networks)
    - In Adversarial training setup, both the agents are competing against each other. The Generator is trying to minimize the log-probability of Discriminator being correct, where as Discriminator is trying to maximize the same. The equilibrium is a saddle point of the Discriminators loss.

    - Loss functions
        - Discriminator Loss : `max log(D(x)) + log(1 - D(G(z)))`
        - Generator Loss : `min log(1 - D(G(z)))`. This loss will suffer from saturating gradient. So, in practice, we use `max log(D(G(z)))`

    - Two competing loss functions make it difficult to optimize. For example, GANs takes a lot of time to converge, they are very sensitive to hyper-parameters, they often suffer from mode collapse, etc.

    - The goal of a GAN is to learn the target distribution. For this, the loss function used has to calculate the distance between the two distributions (fake samples and real samples). The above loss function is very similar to Jensen-Shannon(JS) divergence. But there are other metrics as well, like KL divergence. 

    - Mode Collapse is when your generator model instead of learning the distribution ends up learning a single sample from the target distribution. Irrespective of the input, it always generates the same samples. One way to address Mode collapse is Mini-Batching. Here, you check the variation in the samples generatored by the Generator Network. If the variation is low, then the discriminator can label them as Fake. 

    - Conditional GANs are basically GANs which are conditioned to generate samples that are similar to the input. Example Pix2Pix. But these GANs require a large corpus of corresponding image pairs for training.

    - In GANs, generally there are multiple correct labels. 


2. Another very good playlist that I found is [GANs by Aladdin Persson](https://www.youtube.com/playlist?list=PLhhyoLH6IjfwIp8bZnzX8QR30TRcHO8Va). This playlist will introduce you to GANs in a very systematic manner i.e. new and advance architectures are introduced gradually. It also has paper review and code implementation. So, you can also follow along. 

I will keep updating this list as I learn more.
