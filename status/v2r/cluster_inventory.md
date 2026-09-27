# V2R cluster inventory

2026-09-27T14:43:56.967454+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304749961216 available bytes; 83.00% used; 112401411 free inodes.

server1 `/home`: 304749961216 available bytes; 83.00% used; 112401411 free inodes.

server1 `/tmp`: 304749961216 available bytes; 83.00% used; 112401411 free inodes.

server1 `/var/tmp`: 304749961216 available bytes; 83.00% used; 112401411 free inodes.

server1 `/mnt/raid5`: 630116634624 available bytes; 97.11% used; 337424044 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 13404815360 available bytes; 99.25% used; 110351790 free inodes.

server2 `/home`: 13404815360 available bytes; 99.25% used; 110351790 free inodes.

server2 `/tmp`: 13404815360 available bytes; 99.25% used; 110351790 free inodes.

server2 `/var/tmp`: 13404815360 available bytes; 99.25% used; 110351790 free inodes.

server2 `/mnt/raid5`: 526002098176 available bytes; 96.37% used; 444722072 free inodes.
| server3 | True | ['0', '1'] | [] |

server3 `/`: 78558302208 available bytes; 95.62% used; 114062777 free inodes.

server3 `/home`: 78558302208 available bytes; 95.62% used; 114062777 free inodes.

server3 `/data`: 1328702631936 available bytes; 81.64% used; 225756717 free inodes.

server3 `/tmp`: 78558302208 available bytes; 95.62% used; 114062777 free inodes.

server3 `/var/tmp`: 78558302208 available bytes; 95.62% used; 114062777 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 109761708032 available bytes; 93.87% used; 114372745 free inodes.

server4 `/home`: 109761708032 available bytes; 93.87% used; 114372745 free inodes.

server4 `/data`: 350439276544 available bytes; 95.16% used; 224727329 free inodes.

server4 `/tmp`: 109761708032 available bytes; 93.87% used; 114372745 free inodes.

server4 `/var/tmp`: 109761708032 available bytes; 93.87% used; 114372745 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
