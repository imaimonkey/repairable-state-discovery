# V2R cluster inventory

2026-09-26T02:37:56.356432+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318418436096 available bytes; 82.24% used; 112476271 free inodes.

server1 `/home`: 318418436096 available bytes; 82.24% used; 112476271 free inodes.

server1 `/tmp`: 318418436096 available bytes; 82.24% used; 112476271 free inodes.

server1 `/var/tmp`: 318418436096 available bytes; 82.24% used; 112476271 free inodes.

server1 `/mnt/raid5`: 331162570752 available bytes; 98.48% used; 337546094 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22942281728 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22942281728 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22942281728 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22942281728 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 288761180160 available bytes; 98.00% used; 445054374 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84318355456 available bytes; 95.29% used; 114152374 free inodes.

server3 `/home`: 84318355456 available bytes; 95.29% used; 114152374 free inodes.

server3 `/data`: 124786651136 available bytes; 98.28% used; 225816862 free inodes.

server3 `/tmp`: 84318355456 available bytes; 95.29% used; 114152374 free inodes.

server3 `/var/tmp`: 84318355456 available bytes; 95.29% used; 114152374 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106022961152 available bytes; 94.08% used; 114348272 free inodes.

server4 `/home`: 106022961152 available bytes; 94.08% used; 114348272 free inodes.

server4 `/data`: 109900111872 available bytes; 98.48% used; 224915507 free inodes.

server4 `/tmp`: 106022961152 available bytes; 94.08% used; 114348272 free inodes.

server4 `/var/tmp`: 106022961152 available bytes; 94.08% used; 114348272 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
