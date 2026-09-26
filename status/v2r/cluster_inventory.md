# V2R cluster inventory

2026-09-26T06:02:33.528721+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318778777600 available bytes; 82.22% used; 112476283 free inodes.

server1 `/home`: 318778777600 available bytes; 82.22% used; 112476283 free inodes.

server1 `/tmp`: 318778777600 available bytes; 82.22% used; 112476283 free inodes.

server1 `/var/tmp`: 318778777600 available bytes; 82.22% used; 112476283 free inodes.

server1 `/mnt/raid5`: 227812409344 available bytes; 98.95% used; 337539956 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22736900096 available bytes; 98.73% used; 110405648 free inodes.

server2 `/home`: 22736900096 available bytes; 98.73% used; 110405648 free inodes.

server2 `/tmp`: 22736900096 available bytes; 98.73% used; 110405648 free inodes.

server2 `/var/tmp`: 22736900096 available bytes; 98.73% used; 110405648 free inodes.

server2 `/mnt/raid5`: 274496692224 available bytes; 98.10% used; 445033401 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82439872512 available bytes; 95.40% used; 114110902 free inodes.

server3 `/home`: 82439872512 available bytes; 95.40% used; 114110902 free inodes.

server3 `/data`: 123991306240 available bytes; 98.29% used; 225822758 free inodes.

server3 `/tmp`: 82439872512 available bytes; 95.40% used; 114110902 free inodes.

server3 `/var/tmp`: 82439872512 available bytes; 95.40% used; 114110902 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094018560 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094018560 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106989039616 available bytes; 98.52% used; 224929125 free inodes.

server4 `/tmp`: 106094018560 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094018560 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
