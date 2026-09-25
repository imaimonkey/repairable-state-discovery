# V2R cluster inventory

2026-09-25T08:39:04.017343+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318829961216 available bytes; 82.21% used; 112480381 free inodes.

server1 `/home`: 318829961216 available bytes; 82.21% used; 112480381 free inodes.

server1 `/tmp`: 318829961216 available bytes; 82.21% used; 112480381 free inodes.

server1 `/var/tmp`: 318829961216 available bytes; 82.21% used; 112480381 free inodes.

server1 `/mnt/raid5`: 364211838976 available bytes; 98.33% used; 337557070 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22841057280 available bytes; 98.73% used; 110410486 free inodes.

server2 `/home`: 22841057280 available bytes; 98.73% used; 110410486 free inodes.

server2 `/tmp`: 22841057280 available bytes; 98.73% used; 110410486 free inodes.

server2 `/var/tmp`: 22841057280 available bytes; 98.73% used; 110410486 free inodes.

server2 `/mnt/raid5`: 332960624640 available bytes; 97.70% used; 445093891 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84435738624 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84435738624 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142382096384 available bytes; 98.03% used; 225811527 free inodes.

server3 `/tmp`: 84435738624 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84435738624 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105633759232 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633759232 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 245030961152 available bytes; 96.61% used; 225002922 free inodes.

server4 `/tmp`: 105633759232 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633759232 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
