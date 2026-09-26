# V2R cluster inventory

2026-09-26T05:48:49.358017+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318781620224 available bytes; 82.22% used; 112476278 free inodes.

server1 `/home`: 318781620224 available bytes; 82.22% used; 112476278 free inodes.

server1 `/tmp`: 318781620224 available bytes; 82.22% used; 112476278 free inodes.

server1 `/var/tmp`: 318781620224 available bytes; 82.22% used; 112476278 free inodes.

server1 `/mnt/raid5`: 237564026880 available bytes; 98.91% used; 337540040 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22744539136 available bytes; 98.73% used; 110405661 free inodes.

server2 `/home`: 22744539136 available bytes; 98.73% used; 110405661 free inodes.

server2 `/tmp`: 22744539136 available bytes; 98.73% used; 110405661 free inodes.

server2 `/var/tmp`: 22744539136 available bytes; 98.73% used; 110405661 free inodes.

server2 `/mnt/raid5`: 275380240384 available bytes; 98.10% used; 445033883 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 83187208192 available bytes; 95.36% used; 114148041 free inodes.

server3 `/home`: 83187208192 available bytes; 95.36% used; 114148041 free inodes.

server3 `/data`: 124275089408 available bytes; 98.28% used; 225823931 free inodes.

server3 `/tmp`: 83187208192 available bytes; 95.36% used; 114148041 free inodes.

server3 `/var/tmp`: 83187208192 available bytes; 95.36% used; 114148041 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094415872 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094415872 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106989649920 available bytes; 98.52% used; 224929128 free inodes.

server4 `/tmp`: 106094415872 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094415872 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
