# V2R cluster inventory

2026-09-25T08:06:51.291771+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318842904576 available bytes; 82.21% used; 112480361 free inodes.

server1 `/home`: 318842904576 available bytes; 82.21% used; 112480361 free inodes.

server1 `/tmp`: 318842904576 available bytes; 82.21% used; 112480361 free inodes.

server1 `/var/tmp`: 318842904576 available bytes; 82.21% used; 112480361 free inodes.

server1 `/mnt/raid5`: 386585948160 available bytes; 98.23% used; 337557853 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22843097088 available bytes; 98.73% used; 110410481 free inodes.

server2 `/home`: 22843097088 available bytes; 98.73% used; 110410481 free inodes.

server2 `/tmp`: 22843097088 available bytes; 98.73% used; 110410481 free inodes.

server2 `/var/tmp`: 22843097088 available bytes; 98.73% used; 110410481 free inodes.

server2 `/mnt/raid5`: 333991301120 available bytes; 97.69% used; 445095072 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84436398080 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84436398080 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142390292480 available bytes; 98.03% used; 225812083 free inodes.

server3 `/tmp`: 84436398080 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84436398080 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105625354240 available bytes; 94.11% used; 114350335 free inodes.

server4 `/home`: 105625354240 available bytes; 94.11% used; 114350335 free inodes.

server4 `/data`: 249025187840 available bytes; 96.56% used; 225008817 free inodes.

server4 `/tmp`: 105625354240 available bytes; 94.11% used; 114350335 free inodes.

server4 `/var/tmp`: 105625354240 available bytes; 94.11% used; 114350335 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
