# V2R cluster inventory

2026-09-25T09:31:08.793565+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318837772288 available bytes; 82.21% used; 112480386 free inodes.

server1 `/home`: 318837772288 available bytes; 82.21% used; 112480386 free inodes.

server1 `/tmp`: 318837772288 available bytes; 82.21% used; 112480386 free inodes.

server1 `/var/tmp`: 318837772288 available bytes; 82.21% used; 112480386 free inodes.

server1 `/mnt/raid5`: 350383788032 available bytes; 98.39% used; 337556892 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22829834240 available bytes; 98.73% used; 110410486 free inodes.

server2 `/home`: 22829834240 available bytes; 98.73% used; 110410486 free inodes.

server2 `/tmp`: 22829834240 available bytes; 98.73% used; 110410486 free inodes.

server2 `/var/tmp`: 22829834240 available bytes; 98.73% used; 110410486 free inodes.

server2 `/mnt/raid5`: 331701030912 available bytes; 97.71% used; 445092489 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84419735552 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84419735552 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142298083328 available bytes; 98.03% used; 225810634 free inodes.

server3 `/tmp`: 84419735552 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84419735552 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105623703552 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105623703552 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 241731612672 available bytes; 96.66% used; 224995440 free inodes.

server4 `/tmp`: 105623703552 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105623703552 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
