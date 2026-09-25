# V2R cluster inventory

2026-09-25T10:10:54.809908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318834044928 available bytes; 82.21% used; 112480385 free inodes.

server1 `/home`: 318834044928 available bytes; 82.21% used; 112480385 free inodes.

server1 `/tmp`: 318834044928 available bytes; 82.21% used; 112480385 free inodes.

server1 `/var/tmp`: 318834044928 available bytes; 82.21% used; 112480385 free inodes.

server1 `/mnt/raid5`: 344228044800 available bytes; 98.42% used; 337556408 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22827286528 available bytes; 98.73% used; 110410476 free inodes.

server2 `/home`: 22827286528 available bytes; 98.73% used; 110410476 free inodes.

server2 `/tmp`: 22827286528 available bytes; 98.73% used; 110410476 free inodes.

server2 `/var/tmp`: 22827286528 available bytes; 98.73% used; 110410476 free inodes.

server2 `/mnt/raid5`: 316725182464 available bytes; 97.81% used; 445091104 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417863680 available bytes; 95.29% used; 114156045 free inodes.

server3 `/home`: 84417863680 available bytes; 95.29% used; 114156045 free inodes.

server3 `/data`: 142028058624 available bytes; 98.04% used; 225816261 free inodes.

server3 `/tmp`: 84417863680 available bytes; 95.29% used; 114156045 free inodes.

server3 `/var/tmp`: 84417863680 available bytes; 95.29% used; 114156045 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614065664 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614065664 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240078778368 available bytes; 96.68% used; 224989864 free inodes.

server4 `/tmp`: 105614065664 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614065664 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
