# V2R cluster inventory

2026-09-25T09:34:12.700779+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318837264384 available bytes; 82.21% used; 112480386 free inodes.

server1 `/home`: 318837264384 available bytes; 82.21% used; 112480386 free inodes.

server1 `/tmp`: 318837264384 available bytes; 82.21% used; 112480386 free inodes.

server1 `/var/tmp`: 318837264384 available bytes; 82.21% used; 112480386 free inodes.

server1 `/mnt/raid5`: 350375460864 available bytes; 98.39% used; 337556870 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22828625920 available bytes; 98.73% used; 110410484 free inodes.

server2 `/home`: 22828625920 available bytes; 98.73% used; 110410484 free inodes.

server2 `/tmp`: 22828625920 available bytes; 98.73% used; 110410484 free inodes.

server2 `/var/tmp`: 22828625920 available bytes; 98.73% used; 110410484 free inodes.

server2 `/mnt/raid5`: 331621437440 available bytes; 97.71% used; 445092548 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84419112960 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84419112960 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142301052928 available bytes; 98.03% used; 225810585 free inodes.

server3 `/tmp`: 84419112960 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84419112960 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105623621632 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105623621632 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 241724002304 available bytes; 96.66% used; 224995031 free inodes.

server4 `/tmp`: 105623621632 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105623621632 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
