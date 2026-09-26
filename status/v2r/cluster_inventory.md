# V2R cluster inventory

2026-09-26T11:00:08.917936+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318214131712 available bytes; 82.25% used; 112474832 free inodes.

server1 `/home`: 318214131712 available bytes; 82.25% used; 112474832 free inodes.

server1 `/tmp`: 318214131712 available bytes; 82.25% used; 112474832 free inodes.

server1 `/var/tmp`: 318214131712 available bytes; 82.25% used; 112474832 free inodes.

server1 `/mnt/raid5`: 218761408512 available bytes; 99.00% used; 337538214 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19851599872 available bytes; 98.89% used; 110384899 free inodes.

server2 `/home`: 19851599872 available bytes; 98.89% used; 110384899 free inodes.

server2 `/tmp`: 19851599872 available bytes; 98.89% used; 110384899 free inodes.

server2 `/var/tmp`: 19851599872 available bytes; 98.89% used; 110384899 free inodes.

server2 `/mnt/raid5`: 242321129472 available bytes; 98.33% used; 444979137 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82662580224 available bytes; 95.39% used; 114110819 free inodes.

server3 `/home`: 82662580224 available bytes; 95.39% used; 114110819 free inodes.

server3 `/data`: 123567570944 available bytes; 98.29% used; 225826020 free inodes.

server3 `/tmp`: 82662580224 available bytes; 95.39% used; 114110819 free inodes.

server3 `/var/tmp`: 82662580224 available bytes; 95.39% used; 114110819 free inodes.
| server4 | True | ['3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105926635520 available bytes; 94.09% used; 114347962 free inodes.

server4 `/home`: 105926635520 available bytes; 94.09% used; 114347962 free inodes.

server4 `/data`: 88891830272 available bytes; 98.77% used; 224880565 free inodes.

server4 `/tmp`: 105926635520 available bytes; 94.09% used; 114347962 free inodes.

server4 `/var/tmp`: 105926635520 available bytes; 94.09% used; 114347962 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
