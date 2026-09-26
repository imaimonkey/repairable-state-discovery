# V2R cluster inventory

2026-09-26T07:50:57.293638+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318754521088 available bytes; 82.22% used; 112476267 free inodes.

server1 `/home`: 318754521088 available bytes; 82.22% used; 112476267 free inodes.

server1 `/tmp`: 318754521088 available bytes; 82.22% used; 112476267 free inodes.

server1 `/var/tmp`: 318754521088 available bytes; 82.22% used; 112476267 free inodes.

server1 `/mnt/raid5`: 219194376192 available bytes; 98.99% used; 337539143 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22321000448 available bytes; 98.75% used; 110403907 free inodes.

server2 `/home`: 22321000448 available bytes; 98.75% used; 110403907 free inodes.

server2 `/tmp`: 22321000448 available bytes; 98.75% used; 110403907 free inodes.

server2 `/var/tmp`: 22321000448 available bytes; 98.75% used; 110403907 free inodes.

server2 `/mnt/raid5`: 270650998784 available bytes; 98.13% used; 445026246 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82680414208 available bytes; 95.39% used; 114110871 free inodes.

server3 `/home`: 82680414208 available bytes; 95.39% used; 114110871 free inodes.

server3 `/data`: 123902251008 available bytes; 98.29% used; 225820691 free inodes.

server3 `/tmp`: 82680414208 available bytes; 95.39% used; 114110871 free inodes.

server3 `/var/tmp`: 82680414208 available bytes; 95.39% used; 114110871 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106073817088 available bytes; 94.08% used; 114348162 free inodes.

server4 `/home`: 106073817088 available bytes; 94.08% used; 114348162 free inodes.

server4 `/data`: 105677320192 available bytes; 98.54% used; 224922515 free inodes.

server4 `/tmp`: 106073817088 available bytes; 94.08% used; 114348162 free inodes.

server4 `/var/tmp`: 106073817088 available bytes; 94.08% used; 114348162 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
