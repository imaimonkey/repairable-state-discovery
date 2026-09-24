# V2R cluster inventory

2026-09-24T08:39:28.171260+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324393529344 available bytes; 81.90% used; 112490368 free inodes.

server1 `/home`: 324393529344 available bytes; 81.90% used; 112490368 free inodes.

server1 `/tmp`: 324393529344 available bytes; 81.90% used; 112490368 free inodes.

server1 `/var/tmp`: 324393529344 available bytes; 81.90% used; 112490368 free inodes.

server1 `/mnt/raid5`: 506753294336 available bytes; 97.68% used; 337719514 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57799073792 available bytes; 96.78% used; 110430974 free inodes.

server2 `/home`: 57799073792 available bytes; 96.78% used; 110430974 free inodes.

server2 `/tmp`: 57799073792 available bytes; 96.78% used; 110430974 free inodes.

server2 `/var/tmp`: 57799073792 available bytes; 96.78% used; 110430974 free inodes.

server2 `/mnt/raid5`: 515850211328 available bytes; 96.44% used; 445179194 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85481275392 available bytes; 95.23% used; 114174916 free inodes.

server3 `/home`: 85481275392 available bytes; 95.23% used; 114174916 free inodes.

server3 `/data`: 173687939072 available bytes; 97.60% used; 225822674 free inodes.

server3 `/tmp`: 85481275392 available bytes; 95.23% used; 114174916 free inodes.

server3 `/var/tmp`: 85481275392 available bytes; 95.23% used; 114174916 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105768816640 available bytes; 94.10% used; 114349104 free inodes.

server4 `/home`: 105768816640 available bytes; 94.10% used; 114349104 free inodes.

server4 `/data`: 255369785344 available bytes; 96.47% used; 225288362 free inodes.

server4 `/tmp`: 105768816640 available bytes; 94.10% used; 114349104 free inodes.

server4 `/var/tmp`: 105768816640 available bytes; 94.10% used; 114349104 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
