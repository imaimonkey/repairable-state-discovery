# V2R cluster inventory

2026-09-26T06:25:27.750330+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318769950720 available bytes; 82.22% used; 112476280 free inodes.

server1 `/home`: 318769950720 available bytes; 82.22% used; 112476280 free inodes.

server1 `/tmp`: 318769950720 available bytes; 82.22% used; 112476280 free inodes.

server1 `/var/tmp`: 318769950720 available bytes; 82.22% used; 112476280 free inodes.

server1 `/mnt/raid5`: 219690356736 available bytes; 98.99% used; 337539822 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22315782144 available bytes; 98.76% used; 110403844 free inodes.

server2 `/home`: 22315782144 available bytes; 98.76% used; 110403844 free inodes.

server2 `/tmp`: 22315782144 available bytes; 98.76% used; 110403844 free inodes.

server2 `/var/tmp`: 22315782144 available bytes; 98.76% used; 110403844 free inodes.

server2 `/mnt/raid5`: 273173807104 available bytes; 98.11% used; 445028864 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82565419008 available bytes; 95.39% used; 114110899 free inodes.

server3 `/home`: 82565419008 available bytes; 95.39% used; 114110899 free inodes.

server3 `/data`: 123998711808 available bytes; 98.29% used; 225822365 free inodes.

server3 `/tmp`: 82565419008 available bytes; 95.39% used; 114110899 free inodes.

server3 `/var/tmp`: 82565419008 available bytes; 95.39% used; 114110899 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105914318848 available bytes; 94.09% used; 114346888 free inodes.

server4 `/home`: 105914318848 available bytes; 94.09% used; 114346888 free inodes.

server4 `/data`: 106562531328 available bytes; 98.53% used; 224923519 free inodes.

server4 `/tmp`: 105914318848 available bytes; 94.09% used; 114346888 free inodes.

server4 `/var/tmp`: 105914318848 available bytes; 94.09% used; 114346888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
