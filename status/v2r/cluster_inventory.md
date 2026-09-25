# V2R cluster inventory

2026-09-25T04:40:45.782835+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318914727936 available bytes; 82.21% used; 112480351 free inodes.

server1 `/home`: 318914727936 available bytes; 82.21% used; 112480351 free inodes.

server1 `/tmp`: 318914727936 available bytes; 82.21% used; 112480351 free inodes.

server1 `/var/tmp`: 318914727936 available bytes; 82.21% used; 112480351 free inodes.

server1 `/mnt/raid5`: 408700297216 available bytes; 98.13% used; 337590403 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22946611200 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22946611200 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22946611200 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22946611200 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462168461312 available bytes; 96.81% used; 445109502 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340719616 available bytes; 95.29% used; 114156082 free inodes.

server3 `/home`: 84340719616 available bytes; 95.29% used; 114156082 free inodes.

server3 `/data`: 122695315456 available bytes; 98.30% used; 225815942 free inodes.

server3 `/tmp`: 84340719616 available bytes; 95.29% used; 114156082 free inodes.

server3 `/var/tmp`: 84340719616 available bytes; 95.29% used; 114156082 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105664008192 available bytes; 94.10% used; 114350597 free inodes.

server4 `/home`: 105664008192 available bytes; 94.10% used; 114350597 free inodes.

server4 `/data`: 31175471104 available bytes; 99.57% used; 224962383 free inodes.

server4 `/tmp`: 105664008192 available bytes; 94.10% used; 114350597 free inodes.

server4 `/var/tmp`: 105664008192 available bytes; 94.10% used; 114350597 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
