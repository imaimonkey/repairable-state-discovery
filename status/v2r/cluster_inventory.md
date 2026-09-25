# V2R cluster inventory

2026-09-25T08:40:35.698206+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318829809664 available bytes; 82.21% used; 112480384 free inodes.

server1 `/home`: 318829809664 available bytes; 82.21% used; 112480384 free inodes.

server1 `/tmp`: 318829809664 available bytes; 82.21% used; 112480384 free inodes.

server1 `/var/tmp`: 318829809664 available bytes; 82.21% used; 112480384 free inodes.

server1 `/mnt/raid5`: 364208631808 available bytes; 98.33% used; 337557063 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22840688640 available bytes; 98.73% used; 110410486 free inodes.

server2 `/home`: 22840688640 available bytes; 98.73% used; 110410486 free inodes.

server2 `/tmp`: 22840688640 available bytes; 98.73% used; 110410486 free inodes.

server2 `/var/tmp`: 22840688640 available bytes; 98.73% used; 110410486 free inodes.

server2 `/mnt/raid5`: 332914810880 available bytes; 97.70% used; 445093754 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84435714048 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84435714048 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142381445120 available bytes; 98.03% used; 225811509 free inodes.

server3 `/tmp`: 84435714048 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84435714048 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105633681408 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633681408 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 245028470784 available bytes; 96.61% used; 225002693 free inodes.

server4 `/tmp`: 105633681408 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633681408 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
