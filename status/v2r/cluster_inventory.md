# V2R cluster inventory

2026-09-25T11:02:54.629103+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063465984 available bytes; 82.20% used; 112478858 free inodes.

server1 `/home`: 319063465984 available bytes; 82.20% used; 112478858 free inodes.

server1 `/tmp`: 319063465984 available bytes; 82.20% used; 112478858 free inodes.

server1 `/var/tmp`: 319063465984 available bytes; 82.20% used; 112478858 free inodes.

server1 `/mnt/raid5`: 364840628224 available bytes; 98.33% used; 337555175 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22911238144 available bytes; 98.72% used; 110409988 free inodes.

server2 `/home`: 22911238144 available bytes; 98.72% used; 110409988 free inodes.

server2 `/tmp`: 22911238144 available bytes; 98.72% used; 110409988 free inodes.

server2 `/var/tmp`: 22911238144 available bytes; 98.72% used; 110409988 free inodes.

server2 `/mnt/raid5`: 329012707328 available bytes; 97.73% used; 445088978 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84501643264 available bytes; 95.28% used; 114155531 free inodes.

server3 `/home`: 84501643264 available bytes; 95.28% used; 114155531 free inodes.

server3 `/data`: 142002712576 available bytes; 98.04% used; 225815148 free inodes.

server3 `/tmp`: 84501643264 available bytes; 95.28% used; 114155531 free inodes.

server3 `/var/tmp`: 84501643264 available bytes; 95.28% used; 114155531 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612382208 available bytes; 94.11% used; 114350252 free inodes.

server4 `/home`: 105612382208 available bytes; 94.11% used; 114350252 free inodes.

server4 `/data`: 238652792832 available bytes; 96.70% used; 224983393 free inodes.

server4 `/tmp`: 105612382208 available bytes; 94.11% used; 114350252 free inodes.

server4 `/var/tmp`: 105612382208 available bytes; 94.11% used; 114350252 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
