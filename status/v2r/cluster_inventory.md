# V2R cluster inventory

2026-09-25T12:34:40.271696+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319125958656 available bytes; 82.20% used; 112477613 free inodes.

server1 `/home`: 319125958656 available bytes; 82.20% used; 112477613 free inodes.

server1 `/tmp`: 319125958656 available bytes; 82.20% used; 112477613 free inodes.

server1 `/var/tmp`: 319125958656 available bytes; 82.20% used; 112477613 free inodes.

server1 `/mnt/raid5`: 364278702080 available bytes; 98.33% used; 337548117 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22894505984 available bytes; 98.72% used; 110409958 free inodes.

server2 `/home`: 22894505984 available bytes; 98.72% used; 110409958 free inodes.

server2 `/tmp`: 22894505984 available bytes; 98.72% used; 110409958 free inodes.

server2 `/var/tmp`: 22894505984 available bytes; 98.72% used; 110409958 free inodes.

server2 `/mnt/raid5`: 324450947072 available bytes; 97.76% used; 445079349 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84209475584 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84209475584 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142279081984 available bytes; 98.03% used; 225811137 free inodes.

server3 `/tmp`: 84209475584 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84209475584 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105666011136 available bytes; 94.10% used; 114349723 free inodes.

server4 `/home`: 105666011136 available bytes; 94.10% used; 114349723 free inodes.

server4 `/data`: 231960522752 available bytes; 96.79% used; 224963922 free inodes.

server4 `/tmp`: 105666011136 available bytes; 94.10% used; 114349723 free inodes.

server4 `/var/tmp`: 105666011136 available bytes; 94.10% used; 114349723 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
