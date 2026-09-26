# V2R cluster inventory

2026-09-26T05:51:52.465570+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318780690432 available bytes; 82.22% used; 112476279 free inodes.

server1 `/home`: 318780690432 available bytes; 82.22% used; 112476279 free inodes.

server1 `/tmp`: 318780690432 available bytes; 82.22% used; 112476279 free inodes.

server1 `/var/tmp`: 318780690432 available bytes; 82.22% used; 112476279 free inodes.

server1 `/mnt/raid5`: 235589640192 available bytes; 98.92% used; 337540028 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22739398656 available bytes; 98.73% used; 110405657 free inodes.

server2 `/home`: 22739398656 available bytes; 98.73% used; 110405657 free inodes.

server2 `/tmp`: 22739398656 available bytes; 98.73% used; 110405657 free inodes.

server2 `/var/tmp`: 22739398656 available bytes; 98.73% used; 110405657 free inodes.

server2 `/mnt/raid5`: 274892935168 available bytes; 98.10% used; 445033959 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83188613120 available bytes; 95.36% used; 114148249 free inodes.

server3 `/home`: 83188613120 available bytes; 95.36% used; 114148249 free inodes.

server3 `/data`: 124202369024 available bytes; 98.28% used; 225823875 free inodes.

server3 `/tmp`: 83188613120 available bytes; 95.36% used; 114148249 free inodes.

server3 `/var/tmp`: 83188613120 available bytes; 95.36% used; 114148249 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094297088 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094297088 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106988294144 available bytes; 98.52% used; 224929128 free inodes.

server4 `/tmp`: 106094297088 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094297088 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
