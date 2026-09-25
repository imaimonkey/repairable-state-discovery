# V2R cluster inventory

2026-09-25T08:32:56.917550+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318825308160 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318825308160 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318825308160 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318825308160 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 364225568768 available bytes; 98.33% used; 337557087 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22841896960 available bytes; 98.73% used; 110410490 free inodes.

server2 `/home`: 22841896960 available bytes; 98.73% used; 110410490 free inodes.

server2 `/tmp`: 22841896960 available bytes; 98.73% used; 110410490 free inodes.

server2 `/var/tmp`: 22841896960 available bytes; 98.73% used; 110410490 free inodes.

server2 `/mnt/raid5`: 332615479296 available bytes; 97.70% used; 445094109 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84436361216 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84436361216 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142384582656 available bytes; 98.03% used; 225811629 free inodes.

server3 `/tmp`: 84436361216 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84436361216 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105634050048 available bytes; 94.11% used; 114350327 free inodes.

server4 `/home`: 105634050048 available bytes; 94.11% used; 114350327 free inodes.

server4 `/data`: 245046767616 available bytes; 96.61% used; 225003789 free inodes.

server4 `/tmp`: 105634050048 available bytes; 94.11% used; 114350327 free inodes.

server4 `/var/tmp`: 105634050048 available bytes; 94.11% used; 114350327 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
